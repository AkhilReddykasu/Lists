"""Remove specified index from list and print"""

li = []
n = int(input("enter the length of list:"))
for i in range(0,n):
    ele = int(input("enter the element:"))
    li.append(ele)
print("list before deleting",li)
i = int(input("enter the index you want delete:"))
li.pop(i)
print("list after deleting:",li)





