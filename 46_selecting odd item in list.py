"""Selecting odd items from list"""

li =[]
n = int(input("enter the length:"))
for i in range(0,n):
    ele = int(input("enter an elmnt:"))
    li.append(ele)
print("elements in list",li)
li1 = []
for i in li:
    if i % 2 !=0:
        li1.append(i)

print("odd items in list:",li1)

