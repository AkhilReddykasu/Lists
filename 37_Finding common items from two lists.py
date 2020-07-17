"""Finding common items from two lists"""

li1 = ['akhil', 'kasu', 'bala', 'reddy']
li2 = ['ashrith','akhil','reddy', 'jessy']

'''
def li(l):
    li = []
    n = int(input("enter len of list:"))
    for i in range(0, n):
        ele = input("enter the item:")
        li.append(ele)
    return li


print("values in list 1:", li(li1))
print("values in list 2:", li(li2))
'''

def common_item(a, b):
    A = set(a)
    B = set(b)
    return list(A.intersection(B))


print("common elements between 2 lists", common_item(li1, li2))

