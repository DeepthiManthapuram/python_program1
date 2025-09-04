#sum of factorial of each digit is equal to the number itself
def strong(n):
    sum=0
    a=n
    while(n>0):
        r=n%10
        f=1
        for i in range(1,r+1):
            f = f*i
        sum = sum+f
        n=n//10

    if(sum == a):
        print("strong number")
    else:
        print("not a strong number")
    
strong(int(input("enter any number:")))