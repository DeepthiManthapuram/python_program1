def findFirstLastDigitSum(n):
    l=n%10
    while(n>=10):
        n=n//10
    f=n
    return f+l
print(findFirstLastDigitSum(int(input("enter any number:"))))