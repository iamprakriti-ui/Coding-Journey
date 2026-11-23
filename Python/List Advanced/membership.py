# Splits each input string into a list, using commas as separators
lst1 = input().split(",")
lst2 = input().split(",")
result = []
for element in lst1:
    if element not in lst2:
        result.append(element)
print(result)
