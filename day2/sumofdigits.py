'''def digitsSum(n):
    sum = 0
    for i in str(n):
        sum = sum + int(i)
    return sum

print(digitsSum(input("enter number:")))'''

'''----------------------------------------------------------------------------'''
def digitsSum(n):
    sum = 0
    while(n>0):
        r = n%10
        sum = sum+r
        n= n//10
    return sum

print(digitsSum(int(input("enter number:"))))