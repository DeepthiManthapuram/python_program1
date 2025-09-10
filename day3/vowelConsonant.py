def CountVowelConsonant(str):
    c = 0
    v = 0
    for i in str:
        if(i.isalpha()):
            if(i.lower() in 'aeiou'):
                v += 1
            else:
                c +=1
    print(f"Vowels count: {v}")
    print(f"Consonants count: {c}")

s = input("Enter a string: ")
CountVowelConsonant(s)