lst = input().split(",")
if len(lst) % 2 == 0:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+1]
else:
    lst_mid = lst[len(lst)//2-1:len(lst)//2+2]
print(lst_mid)
