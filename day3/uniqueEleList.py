def uniqueEle(mylist):
    list1=[]
    for i in mylist:
        if(i not in list1):
            list1 = list1 +[i]
    return list1

mylist=eval(input("enter list:"))
print(uniqueEle(mylist))