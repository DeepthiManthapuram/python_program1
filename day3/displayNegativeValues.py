def displayNegative(mylist):
    for i in mylist:
        if(i<0):
            print(i,end=" ")

mylist=eval(input("enter list:"))
print(displayNegative(mylist))