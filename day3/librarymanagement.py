
def addBook(id,title,dict1): 
    if(id in dict1):
        print("Book is already present")
    else:
        dict1[id] = title
        print("Book added successfully")
    return dict1

def removeBook(id,dict1):
    del dict1[id]
    return dict1
        
def searchBook(id,dict1):
    for key,value in dict1.items():
        if(key == id):
            print(f"Book named {value}")
            
def updateTitle(id,title,dict1):
    dict1[id] = title
    return dict1

def displayBooks(dict1):
    for key,value in dict1.items():
        print(f"Book id: {key}, Book title: {value}")

def countBooks(dict1):
    return len(dict1)



choice = int(input("1.Add Book\n2.Remove Book\n3.Search Book\n4.Update Title\n5.Display Books\n6.Count Books\nEnter your choice: "))
dict1 = {'101':'Python Programming', '102':'Java Programming', '103':'Web Development', '104':'Data Science'}

if(choice == 1):
    id = input("enter book id: ")
    title = input("enter book title: ")
    print(addBook(id,title,dict1))
elif(choice == 2):
    id = input("enter book id: ")    
    print(removeBook(id,dict1))
elif(choice == 3):
    id = input("enter book id: ")
    searchBook(id,dict1)
elif(choice == 4):
    id = input("enter book id: ")
    print(updateTitle(id,title,dict1))
    title = input("enter book title: ")
elif(choice == 5):
    displayBooks(dict1)
elif(choice == 6):
    print(countBooks(dict1))
