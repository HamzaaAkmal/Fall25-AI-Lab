def remove_punctuations(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for ch in text:
        if ch not in punctuations:
            result += ch
    return result

# Example usage
sentence = "Hello!!! How are you? I'm fine..."
print("Original:", sentence)
print("Without Punctuations:", remove_punctuations(sentence))
