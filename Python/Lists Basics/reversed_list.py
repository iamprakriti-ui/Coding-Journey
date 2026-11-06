def reverse(lst):
    res = []
    for i in range(len(lst)):
        res.append(lst[len(lst) - i - 1])
    return res
