from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pickle
import numpy as np
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

# Load the trained model and metadata
MODEL_PATH = 'crypto_price_model.pkl'
METADATA_PATH = 'model_metadata.pkl'
FEATURES_PATH = 'feature_names.pkl'

# Global variables for model and metadata
model = None
metadata = None
feature_names = None

def load_model():
    """Load the trained model and metadata"""
    global model, metadata, feature_names
    
    try:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        print("Model loaded successfully!")
        
        with open(METADATA_PATH, 'rb') as f:
            metadata = pickle.load(f)
        print(f"Model metadata loaded: {metadata['model_name']}")
        
        with open(FEATURES_PATH, 'rb') as f:
            feature_names = pickle.load(f)
        print(f"Feature names loaded: {len(feature_names)} features")
        
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        return False

@app.route('/')
def home():
    """Serve the main HTML page"""
    return render_template('index.html')

@app.route('/api/model-info', methods=['GET'])
def model_info():
    """Get information about the model"""
    if metadata is None or feature_names is None:
        return jsonify({'error': 'Model not loaded'}), 500
    
    return jsonify({
        'model_name': metadata['model_name'],
        'r2_score': float(metadata['r2_score']),
        'target': metadata['target'],
        'features': feature_names,
        'num_features': len(feature_names)
    })

@app.route('/api/predict', methods=['POST'])
def predict():
    """Make a prediction based on input features"""
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        # Get JSON data from request
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Extract features in the correct order
        features = []
        missing_features = []
        
        for feature_name in feature_names:
            if feature_name in data:
                features.append(float(data[feature_name]))
            else:
                missing_features.append(feature_name)
        
        if missing_features:
            return jsonify({
                'error': 'Missing features',
                'missing': missing_features
            }), 400
        
        # Make prediction
        features_array = np.array([features])
        prediction = model.predict(features_array)[0]
        
        return jsonify({
            'success': True,
            'prediction': float(prediction),
            'model_used': metadata['model_name'],
            'target': metadata['target']
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/predict-simple', methods=['POST'])
def predict_simple():
    """
    Simplified prediction endpoint that accepts key features
    and uses default values for others
    """
    try:
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        data = request.get_json()
        
        # Load a sample from the CSV to get default values
        sample_data = pd.read_csv('clean_crypto_data.csv')
        default_values = sample_data[feature_names].iloc[-1].to_dict()
        
        # Update with user-provided values
        for key, value in data.items():
            if key in default_values:
                default_values[key] = float(value)
        
        # Create features array
        features = [default_values[feat] for feat in feature_names]
        features_array = np.array([features])
        
        # Make prediction
        prediction = model.predict(features_array)[0]
        
        return jsonify({
            'success': True,
            'prediction': float(prediction),
            'model_used': metadata['model_name'],
            'target': metadata['target'],
            'features_used': data
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Load the model on startup
    if load_model():
        print("\n" + "="*50)
        print("Flask API Server Starting...")
        print(f"Model: {metadata['model_name']}")
        print(f"R2 Score: {metadata['r2_score']:.4f}")
        print(f"Features: {len(feature_names)}")
        print("="*50 + "\n")
        app.run(debug=True, host='0.0.0.0', port=5000)
    else:
        print("Failed to load model. Please run train_and_save_model.py first.")
