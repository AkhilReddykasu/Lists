"""largest no in list"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)

print("maximum no in list",max(li1))