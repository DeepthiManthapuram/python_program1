class Student:
    def __init__(self,name,branch,marks):
        self.name = name #public
        self.branch = branch #public
        self.__marks = marks #private
    def display(self):
        print("Name:",self.name)
        print("Branch:",self.branch)
        print("Marks:",self.__marks)

obj = Student("priya","CSE",89)
obj2 = Student("anitha","ECE",95)
obj.display()
obj2.display()