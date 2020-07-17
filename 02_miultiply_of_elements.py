"""multiply of elements"""

li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li1.append(ele)

def mul_li(l):
    result = 1
    for i in l:
        result = result * i
    return result

print("multily values in list",mul_li(li1))



