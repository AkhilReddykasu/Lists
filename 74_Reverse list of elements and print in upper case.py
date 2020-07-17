"""Reverse list of elements and print in upper case	"""


li1 = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = input("enter element:")
    li1.append(ele)
def upper_case(l):
    i = tuple(l)
    z = i.upper()
    return z[::-1]


print("reverse elem:",(upper_case(li1)))
