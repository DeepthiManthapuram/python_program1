def studentDetails(student_list):
    max=0
    for i in student_list:
        if(i[2] > max):
            max = i[2]

    for i in student_list:
        if(i[2] == max):
            print(f"{i[1]} got highest marks")

    list2 = []
    for i in student_list:
        if(i[2] > 75):
            more_than_75 = i[1]
            list2.append(more_than_75)
    print("Students who scored more than 75 marks are:",list2)

stud_list = []
stud_tup = ()
for i in range(1,6):
    roll = input("Enter the roll number: ")
    name = input("Enter the name: ")
    marks = int(input("Enter the marks: "))
    stud_tup = (roll,name,marks)
    stud_list.append(stud_tup)
studentDetails(stud_list)