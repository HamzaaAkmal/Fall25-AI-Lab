text = "kuch,Bhi;KuchBhi!" 

class Punctuation:
    def __init__(self, text):
        self.text = text
        self.check_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    def remove_char(self):
        result = ""
        for ch in self.text:
            if ch not in self.check_char:   
                result += ch
        return result
p = Punctuation(text)
clean_text = p.remove_char()
print("Original:", text)
print("Without punctuation:", clean_text)