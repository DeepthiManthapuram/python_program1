#To check whether a number is perfect or not
def perfectNumberCheck(n):
    sum = 0
    for i in range(1,n+1):
        if(n%i == 0):
            sum = sum + i
    if(sum == 2*n):
        print("perfect number")
    else:
        print("not a perfect number")

num = int(input("enter any number:"))
perfectNumberCheck(num)