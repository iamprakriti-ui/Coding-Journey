lst = input().split(",")
slice1 = lst[1::3]
slice2 = lst[5::-1]
middle = len(lst)//2
slice3 = lst[middle::2]
print(slice1)
print(slice2)
print(slice3)
