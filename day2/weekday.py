def week(n):
    if(n == 0):
        return "Sunday"
    elif(n == 1):
        return "Monday"
    elif(n == 2):
        return "Tuesday"
    elif(n == 3):
        return "wednesday"
    elif(n == 4):
        return "thursday"
    elif(n == 5):
        return "friday"
    elif(n == 6):
        return "saturday"

day = int(input("enter any day:"))  
print(week(day))