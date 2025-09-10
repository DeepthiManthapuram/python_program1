def eleFrequent(mylist):
    list1=[]
    for i in mylist:
        if(i not in list1):
            list1 = list1 +[i]
    for i in list1:
        c=0
        for j in mylist:
            if(i == j):
                c += 1
        print(f"{i} -> {c}")

mylist=eval(input("enter list:"))
eleFrequent(mylist)