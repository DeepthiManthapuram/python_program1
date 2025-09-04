def toCheckAlphaDigitSpecial(ch):
    if(ch >= 'a' and ch <= 'z') or (ch >= 'A' and ch <= 'Z'):
        return "Alphabet"
    elif(ch >= '0' and ch <= '9'):
        return "Digit"
    else:
        return "Special Character"
    
c = input("Enter any character:")
print(toCheckAlphaDigitSpecial(c))