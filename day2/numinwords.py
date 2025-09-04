def numInWords(n):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    s=""
    for i in str(n):
        s=s+d[int(i)]+" "
    return s
print(numInWords(int(input("enter any number:"))))