def fun(list, x, y):  
    
    charOfList = len(list)
    list2 = [x]*(y)

    if (charOfList%2 == 1):
        middleOfList =(charOfList//2) + 1
    else:
        middleOfList = charOfList//2

    if (charOfList%2 == 0):
        cutList1 = list[:middleOfList]
        cutList2 = list[middleOfList:]
        list = cutList1+list2+cutList2

    else:
        list.extend(list2)

    return list

def form(list, index):
    total = 0
    charOfList = len(list)
    if (index > charOfList):
        return 0
    else:
        total = list[charOfList-index]*(10**(index-1)) + form (list, index + 1)
        return total


lst = [1,3,5,7,9]
print(lst)
lst = fun(lst, 4, 3)
print(lst)
print(form(lst, 1))