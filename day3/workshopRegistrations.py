def workshopRegistrations(day1,day2,day3):
    day1_set = set(day1)
    day2_set = set(day2)
    day3_set = set(day3)
    print("total number of attendees in day1:",len(day1_set))
    print("total number of attendees in day2:",len(day2_set))
    print("total number of attendees in day3:",len(day3_set))

    regular_attendees = []
    for i,j,k in zip(day1,day2,day3):
        if(i == j and j == k):
            regular_attendees.append(i)
    print("Regular attendees in all three days are:",regular_attendees)

    one_day_attendees = []
    for i in day1:
        if(i not in day2 and i not in day3):
            one_day_attendees.append(i)
    print("Attendees who attended only day1 are:",one_day_attendees)


    for i in day1:
        for j in day2:
            c = 0
            if(i == j):
                c += 1
        print("count attendees for day1 and day2: ",c)

    for i in day2:
        for j in day3:
            c = 0
            if(i == j):
                c += 1
        print("count attendees for day2 and day3: ",c)

    for i in day1:
        for j in day3:
            c = 0
            if(i == j):
                c += 1
        print("count attendees for day1 and day3: ",c)

    print("Final report:")
    print("day1 attendees : ",day1_set)
    print("day2 attendees : ",day2_set)
    print("day3 attendees : ",day3_set)
    print("Regular attendees in all three days are:",regular_attendees)
    print("Attendees who attended only day1 are:",one_day_attendees)
    print("count attendees for day1 and day2: ",c)
    print("count of attendees for day2 and day3: ",c)
    print("count of attendees for day1 and day3: ",c)



d1 = ["alice@gmail.com","bob@gmail.com","cob@gmail.com"]
d2 = ["slice@gmail.com","mice@gmail.com","rice@gmail.com","rice@gmail.com","flice@gmail.com","alice@gmail.com"]
d3 = ["Alice@gmail.com","flIce@gmail.com","alice@gmail.com"]
print(workshopRegistrations(d1,d2,d3))