def armstrong(n):
    sum = 0
    a=n
    while(n>0):
        r = n%10
        sum = sum+r**3
        n= n//10
    if(sum == a):
        print("armstrong number")
    else:
        print("not an armstrong number")

armstrong(int(input("enter number:")))