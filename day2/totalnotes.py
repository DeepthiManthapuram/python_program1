def totalNotes(amount):
    notes_list = [500,100,50,20,10]
    notes={}
    for i in notes_list:
        if(amount >= i):
            notes[i] = amount//i
            amount = amount % i
    return notes

a=int(input("enter amount:"))
print(totalNotes(a))