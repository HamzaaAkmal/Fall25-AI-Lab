sentence = "Hey! I'm Hamza Akmal Founder/CEO of downlabs."

words = sentence.split()

for i in range(len(words)):
    min_index = i
    for j in range(i+1, len(words)):
        if ord(words[j][0]) < ord(words[min_index][0]):
            min_index = j
    if min_index != i:
        words[i], words[min_index] = words[min_index], words[i]

sorted_sentence = " ".join(words)

print("Original:", sentence)
print("Sorted:", sorted_sentence)