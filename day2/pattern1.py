def squarePattern(n):
    for i in range(n):
        for j in range(n):
            print("* ",end="")
        print()
print(squarePattern(int(input("enter number of rows:"))))
    