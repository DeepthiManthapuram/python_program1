def palindrome(n):
    for i in range(10,n+1):
        temp=i
        rev=0
        for j in range(len(str(i))):
            r=i%10
            rev=rev*10+r
            i=i//10
        if(rev == temp):
            print(temp,end=" ")




palindrome(int(input("enter any number:")))