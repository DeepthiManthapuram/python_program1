c_num = int(input("Enter current bill number: "))
c_name = input("Enter current customer name: ")
p_read = float(input("Enter present month reading:"))
l_read = float(input("Enter last month reading:"))

total_units = p_read - l_read
bill = total_units*3.80

print("****current bill details****")
print("current bill number:",c_num)
print("current customer name:",c_name)
print("present month reading:", p_read)
print("last month reading:",l_read)
print("total units consumed:",round(total_units,2))
print("amount to be paid:",round(bill,3))