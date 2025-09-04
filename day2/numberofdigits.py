def numberOfDigits(n):
    c=0
    for i in str(n):
        c=c+1
    return c

print(numberOfDigits(int(input("enter number:"))))