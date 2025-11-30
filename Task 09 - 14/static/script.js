// Global variables
let modelInfo = null;
let allFeatures = [];

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    loadModelInfo();
    setupEventListeners();
});

// Load model information from API
async function loadModelInfo() {
    try {
        const response = await fetch('/api/model-info');
        const data = await response.json();
        
        if (data.error) {
            showError('Failed to load model information: ' + data.error);
            return;
        }
        
        modelInfo = data;
        allFeatures = data.features;
        
        // Update UI with model info
        document.getElementById('modelName').textContent = data.model_name;
        document.getElementById('modelScore').textContent = data.r2_score.toFixed(4);
        document.getElementById('modelTarget').textContent = data.target;
        
        // Generate advanced form fields
        generateAdvancedForm(data.features);
        
    } catch (error) {
        showError('Error loading model information: ' + error.message);
    }
}

// Generate form fields for advanced mode
function generateAdvancedForm(features) {
    const container = document.getElementById('advancedFormFields');
    container.innerHTML = '';
    
    features.forEach(feature => {
        const formGroup = document.createElement('div');
        formGroup.className = 'form-group';
        
        const label = document.createElement('label');
        label.setAttribute('for', feature);
        label.textContent = feature;
        
        const input = document.createElement('input');
        input.type = 'number';
        input.id = feature;
        input.name = feature;
        input.step = 'any';
        input.required = true;
        
        formGroup.appendChild(label);
        formGroup.appendChild(input);
        container.appendChild(formGroup);
    });
}

// Setup event listeners
function setupEventListeners() {
    // Simple form submission
    document.getElementById('simplePredictionForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        await handleSimplePrediction(e.target);
    });
    
    // Advanced form submission
    document.getElementById('advancedPredictionForm').addEventListener('submit', async (e) => {
        e.preventDefault();
        await handleAdvancedPrediction(e.target);
    });
}

// Handle simple prediction
async function handleSimplePrediction(form) {
    hideResults();
    hideError();
    
    const formData = new FormData(form);
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        data[key] = parseFloat(value);
    }
    
    try {
        const response = await fetch('/api/predict-simple', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.error) {
            showError('Prediction error: ' + result.error);
            return;
        }
        
        showResults(result);
        
    } catch (error) {
        showError('Error making prediction: ' + error.message);
    }
}

// Handle advanced prediction
async function handleAdvancedPrediction(form) {
    hideResults();
    hideError();
    
    const formData = new FormData(form);
    const data = {};
    
    for (let [key, value] of formData.entries()) {
        data[key] = parseFloat(value);
    }
    
    try {
        const response = await fetch('/api/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        });
        
        const result = await response.json();
        
        if (result.error) {
            if (result.missing) {
                showError(`Missing features: ${result.missing.join(', ')}`);
            } else {
                showError('Prediction error: ' + result.error);
            }
            return;
        }
        
        showResults(result);
        
    } catch (error) {
        showError('Error making prediction: ' + error.message);
    }
}

// Show results
function showResults(result) {
    const resultsDiv = document.getElementById('results');
    const predictionValue = document.getElementById('predictionValue');
    const resultModel = document.getElementById('resultModel');
    const predictionTime = document.getElementById('predictionTime');
    
    // Format the prediction value as currency
    predictionValue.textContent = '$' + result.prediction.toFixed(2);
    resultModel.textContent = result.model_used;
    predictionTime.textContent = new Date().toLocaleString();
    
    resultsDiv.classList.remove('hidden');
    
    // Scroll to results
    resultsDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Show error message
function showError(message) {
    const errorDiv = document.getElementById('error');
    const errorMessage = document.getElementById('errorMessage');
    
    errorMessage.textContent = message;
    errorDiv.classList.remove('hidden');
    
    // Scroll to error
    errorDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

// Hide results
function hideResults() {
    document.getElementById('results').classList.add('hidden');
}

// Hide error
function hideError() {
    document.getElementById('error').classList.add('hidden');
}

// Switch between tabs
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.remove('active');
    });
    
    // Remove active class from all buttons
    document.querySelectorAll('.tab-button').forEach(button => {
        button.classList.remove('active');
    });
    
    // Show selected tab
    if (tabName === 'simple') {
        document.getElementById('simpleTab').classList.add('active');
        document.querySelector('[onclick="switchTab(\'simple\')"]').classList.add('active');
    } else {
        document.getElementById('advancedTab').classList.add('active');
        document.querySelector('[onclick="switchTab(\'advanced\')"]').classList.add('active');
    }
    
    // Hide results and errors when switching tabs
    hideResults();
    hideError();
}

// Format number as currency
function formatCurrency(value) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
        maximumFractionDigits: 2
    }).format(value);
}
