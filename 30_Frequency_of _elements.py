"""Frequency of Elements"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print(li1)
i = int(input("enter the element to know the frequency:"))
print("frequency of element:",li1.count(i))


