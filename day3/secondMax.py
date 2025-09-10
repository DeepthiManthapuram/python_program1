def secondMaxEle(mylist):
    mylist.sort()
    return mylist[-2]

mylist=eval(input("enter list:"))
print(secondMaxEle(mylist)) 