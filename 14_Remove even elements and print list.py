"""Removing even elements from the lis"""

li = []
n = int(input("enter the legth of list:"))
for i in range(0,n):
    ele = int(input("enter the elements:"))
    li.append(ele)
l1 = []
for i in li:
    if i % 2 !=0:
        l1.append(i)
print("After removing even elements in the list:",l1)


