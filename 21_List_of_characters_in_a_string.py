"""List of characters in a String"""

li = []
n = int(input("enter the len:"))
for i in range(0,n):
    ele = input("enter a string of charcters:")
    li.append(ele)
print("elements in list:",li)
j = input("enter the sting ")
if j in li:
    print("characters in a string:",len(j))
else:
    print("not available")
