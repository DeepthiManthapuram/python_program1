#Pascal triangle

from math import factorial

def pascalTriangle(n):
    for i in range(1,n+1):
        for j in range(i):
            print(factorial(i-1)//(factorial(j)*factorial(i-j-1)),end = " ")
        print()

num = int(input("enter a number"))
pascalTriangle(num)