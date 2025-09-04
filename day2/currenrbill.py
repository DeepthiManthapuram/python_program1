
def currentBill(c_num,c_name,p_read,l_read):
    total_units = p_read - l_read
    if(total_units>=1 or total_units<=50):
        bill = total_units*3.80
    elif(total_units>=51 or total_units<100):
        bill = 50*3.80 + (total_units - 50)*4.20
    elif(total_units>=100 or total_units<200):
        bill = 50*3.80 + 50*4.20+(total_units - 100)*5.10
    elif(total_units>=200 or total_units<300):
        bill = 50*3.80 + 50*4.20 + 100*5.10 + (total_units - 200)*6.30
    elif(total_units>=300):
        bill = 50*3.80 + 50*4.20 + 100*5.10 + 100*6.30 + (total_units - 300)*7.50
    return total_units,bill


c_num = int(input("Enter current bill number: "))
c_name = input("Enter current customer name: ")
p_read = float(input("Enter present month reading:"))
l_read = float(input("Enter last month reading:"))

total_units,bill = currentBill(c_num,c_name,p_read,l_read)

print("****current bill details****")
print("current bill number:",c_num)
print("current customer name:",c_name)
print("present month reading:", p_read)
print("last month reading:",l_read)
print("total units consumed:",round(total_units,2))
print("amount to be paid:",round(bill,3))