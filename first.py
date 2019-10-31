mylist = list(range(4))
seclist = mylist
print (seclist)
mylist.append(4)
print (seclist)
seclist = mylist[:]
print (seclist)
mylist.append(5)
print (seclist)
mylist.append(6)
print(seclist)


# -----------The above code will gives the following output----------

# [0, 1, 2, 3]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]
# [0, 1, 2, 3, 4]

