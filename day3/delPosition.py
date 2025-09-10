def delSpecificPosition(mylist,pos):
    if(pos<0 or pos>len(mylist)):
        return "invalid position"
    else:
        list1=[]
        for i in range(len(mylist)):
            if(i == pos):
                continue
            else:
                list1 = list1 +[mylist[i]]
        return list1

mylist=eval(input("enter list:"))
p=int(input("enter position to be deleted:"))
print(delSpecificPosition(mylist,p))