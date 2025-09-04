def primeCheck(n):
    if(n<=1):
        return f"{n} is not a prime number"
    else:
        
        for i in range(2,n+1):
            c=0
            for j in range(1,i+1):
                if(i%j==0):
                    c=c+1
            if(c==2):
                print(i,end=" ")
                    
            
primeCheck(int(input("enter a number:")))