# 10.Create a suitable object type to eliminate the duplicate elements
lst=[11, 22, 33, 11, 11, 50, 33, 22]
fnl = []


def duplicate_removal(lst):
    for i in lst:
        if i not in fnl:  
            fnl.append(i)
    return fnl
print(duplicate_removal(lst))
