def lowestFrequency(str1):
    unique_char = ""
    for i in str1:
        if(i not in unique_char):
            unique_char += i
    freq = []
    for i in unique_char:
        c = 0
        for j in str1:
            if i == j:
                c += 1
        tuple1 = (i,c)
        freq.append(tuple1)
    freq_list = []
    for i in freq:
        freq_list.append(i[1])
    min_freq = min(freq_list)
    for i in freq:
        if i[1] == min_freq:
            return i[0]


s = input("Enter a string: ")
print(lowestFrequency(s))        