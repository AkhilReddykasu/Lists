"""Shuffle list and print"""
import random
li = []
len = int(input("enter the length of list:"))
for i in range(0,len):
    ele = int(input("enter element:"))
    li.append(ele)
print("elements in list",li)
random.shuffle(li)
print("elements in list",li)

