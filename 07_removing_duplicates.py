"""Removing duplicates"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print(li1)
A = set(li1)
li1 = list(A)
print("After removing duplicate elements:", li1)