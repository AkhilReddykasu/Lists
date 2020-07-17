"""Difference between two lists"""



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
"""
def diff_ele(a , b):
    A = set(a)
    B = set(b)
    return A - B

print("common elements between 2 lists",diff_ele(li1,li2))
"""

def diff_ele(x, y):
    li3 =[]
    for i in x + y:
        if i not in x or i not in y:
            li3.append(i)
    return li3

print("difference between two elements:",diff_ele(li1, li2))
