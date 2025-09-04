def studentStatus(roll,name,total):

    if(total>=40):
        if(total<50):
            return f"student details:\nstudent number:{roll}\nstudent name:{name}\ngrade:C\n"
        elif(total>=51 and total<=70):
            return f"student details:\nstudent number:{roll}\nstudent name:{name}\ngrade:B\n"
        elif(total>=71 and total<=80):
            return f"student details:\nstudent number:{roll}\nstudent name:{name}\ngrade:A\n"
        else:
            return f"student details:\nstudent number:{roll}\nstudent name:{name}\ngrade:A+\n"
    else:
        return "FAIL"     
        
    
roll=int(input("enter student number:"))
name=input("enter student name:")
p = int(input("enter marks in physics:"))
c = int(input("enter marks in chemistry:"))
m = int(input("enter marks in maths:"))
total = p+c+m
print(studentStatus(roll,name,total))
