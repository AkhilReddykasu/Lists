"""Finding an index of a specified element in list"""


li1 = []
m = int(input("enter the length of list:"))
for i in range(0,m):
    ele = int(input("enter element:"))
    li1.append(ele)
print('elements in list:',li1)
n = int(input("enter the elemnet to know the index:"))
if n in li1:
    print("index of ",n,"is:",li1.index(n))
else:
    print("element not available")

