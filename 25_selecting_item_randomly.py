"""selecting item randomly and print index and values"""


li = []
n = int(input("enter the length:"))
for i in range(0,n):
    ele = int(input("enter an element:"))
    li.append(ele)
i = int(input("enter the value you want search for:"))
if i in li:
    print("searched element is available")
    print("index of element",li.index(i))
else:
    print("element not found")



















