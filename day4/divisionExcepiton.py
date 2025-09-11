class ExceptionDivision:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def divide(self):
        try:
            res = self.a/self.b
            return res
        
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed"

num = int(input("Enter numerator: "))
den = int(input("Enter denominator: "))     
obj = ExceptionDivision(num,den)
print(obj.divide())
