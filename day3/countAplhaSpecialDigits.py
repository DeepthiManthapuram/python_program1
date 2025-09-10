def countAlphabetsDigitsSpecial(str):
    a = 0
    d = 0
    s = 0
    for i in str:
        if(i.isalpha()):
            a += 1
        elif(i.isdigit()):
            d += 1
        else:
            s += 1
    print(f"Alphabets: {a}, Digits: {d}, Special Characters: {s}")


s = input("Enter a string: ")
countAlphabetsDigitsSpecial(s)