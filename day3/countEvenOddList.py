def evenOddCount(mylist):
    e=0
    odd=0
    for i in mylist:
        if(i%2 == 0):
            e+=1
        else:
            odd+=1
    return e,odd

mylist=eval(input("enter list:"))
print(evenOddCount(mylist))
