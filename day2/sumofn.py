def naturalNumbersSum(n):
    i=1
    sum = 0
    while(i<=n):
        sum = sum+i
        i=i+1
    return sum
num = int(input("enter any number:"))
print(naturalNumbersSum(num))