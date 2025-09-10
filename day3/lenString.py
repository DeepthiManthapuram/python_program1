def StringLength(str):
    count = 0
    for i in str:
        count += 1
    return count

def compareStrings(str1,str2):
    if(str1 == str2):
        return "both strings are equal"
    if(str1 < str2):
        return f"{str1} is less than {str2}"
    else:
        return f"{str1} is greater than {str2}"
    
def concatenateStrings(str1,str2):
    return str1 + str2

s = input("Enter a string: ")
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
print(StringLength(s))
print(concatenateStrings(s1,s2))
print(compareStrings(s1,s2))