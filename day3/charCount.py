def charCount(str1):
    unique_char = ""
    for i in str1:
        if(i not in unique_char):
            unique_char += i
    final_str = ""
    for i in unique_char:
        c = 0
        for j in str1:
            if i == j:
                c += 1
        final_str += i + str(c)
    return final_str



s = input("Enter a string: ")
print(charCount(s))