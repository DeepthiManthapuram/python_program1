class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.salary)

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department
    
    def display(self):
        super().display()
        print("Department:",self.department)

#emp_obj = Employee("priya",50000)
man_obj = Manager("rahul",70000,"IT")
#emp_obj.display()
man_obj.display()