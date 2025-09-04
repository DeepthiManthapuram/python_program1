def factorial(n):
    if(n<=0):
        return 0
    else:
        f=1
        while(n>0):
            f = f*n
            n = n-1
        return f
    
print(factorial(int(input("enter any number:"))))