def merge(lst1, lst2):
    res = []
    for i in range(len(lst2)):
        res.append(lst2[i])
    for i in range(len(lst1)):
        res.append(lst1[i])
    res.sort()
    return res
