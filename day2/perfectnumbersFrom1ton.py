#To display all perfect numbers from 1 to n
def perfectNumberCheck(n):
    
    for i in range(1,n+1):
        sum = 0
        for j in range(1,i):
            if(i%j == 0):
                sum = sum + j
        if(sum == i):
            print(i,end=" ")
    
num = int(input("enter any number:"))
perfectNumberCheck(num)