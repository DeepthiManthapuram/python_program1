def primeCheck(n):
    if(n<=1):
        return f"{n} is not a prime number"
    else:
        i=2
        while(i<n):
            if(n%i == 0):
                return f"{n} is not a prime number"
            i = i+1
    return f"{n} is a prime number"
            
print(primeCheck(int(input("enter a number:"))))