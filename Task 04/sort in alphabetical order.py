text = "I am Rasikh"
arr = list(text) 
print(arr)
length = len(arr)
for i in range(length):
    for j in range(i+1, length):
        if ord(arr[j]) < ord(arr[i]):   
            char = arr[i]
            arr[i] = arr[j]
            arr[j] = char

print("Original:", text)
print("Sorted by alphabet:", ''.join(arr))