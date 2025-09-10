def countWords(str):
    
    words = str.split(" ")
    return len(words)

s = input("Enter a string: ")
print(countWords(s))