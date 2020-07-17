"""elements in Ascending order"""


li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print("elements bed=fore ascending order",li1)
li1.sort(reverse=False)
print("elements in ascending order:",li1)