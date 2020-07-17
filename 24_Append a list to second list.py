""""Append a list to second list"""


li1 = []
li2 = []
def ele_list(l):
    n = int(input("enter the length of list:"))
    for i in range(0,n):
        ele = int(input("enter the element:"))
        l.append(ele)
    return l
print("elements in list 1:",ele_list(li1))
print("elements in list 2:",ele_list(li2))

li3 = li2 + li1
print(li3)