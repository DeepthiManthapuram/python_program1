def duplicateCount(mylist):
    list1=[]
    for i in mylist:
        if(i not in list1):
            list1 = list1 +[i]
    count_list=[]
    for i in list1:
        c=0
        for j in mylist:
            if(i == j):
                c += 1
        count_list = count_list + [c]

    for i,j in zip(list1,count_list):
        if(j>1):
            print(f"{i}->{j}")

mylist=eval(input("enter list:"))
duplicateCount(mylist)