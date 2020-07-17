"""Finding a second smallest number"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print(li1)
li1.sort()
print("second smallest",li1[1])

