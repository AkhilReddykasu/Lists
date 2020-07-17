"""Counting number elements within a specified ranges"""


li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)
print(li1)

def el_sprange(l,a):
    li =[]
    r = int(a)
    for i in range(l.index(r),len(l)):
        li = li + i

    return li
r = input("enter the element you want to start from:")
print("Counting number elements within a specified ranges:",el_sprange(li1,r))
