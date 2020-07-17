"""To access index of list"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print('elements in list:',li1)
n = int(input("enter the index:"))
print("element in index is:",li1[n])





















