# 6.	Create 3 Lists ( list1,list2,list3) with numbers and perform following operations
#         a) Create Maxlist by taking 2 maximum elements from each list.
#         b) Find average value from all the elements of Maxlist.
#         c) Create a MinlIst by taking 2 minimum elements from each list 
#         d) Find the average value from all the elements of Minlist

lst1 = [5, 4, 3, 2, 1]
lst2 = [50, 40, 30, 20, 10]
lst3 = [55, 44, 33, 22, 11]
idx = ["lst1", "lst2", "lst3"]
max_lst = []
min_lst = []

# Creating maxlist by taking two maximum elements from each list
for i in range(1, 3):
    list(idx[i]).sort()
    list(idx[i]).reverse()

for i in range(0, 2):
    max_lst.append(lst1[i])
    max_lst.append(lst2[i])
    max_lst.append(lst3[i])

max_lst.sort()
print("---------- Maxlist by taking two elements from each list-----------")
print(max_lst)

# Finding average of maxlist
print("---------- Average of Maxlist ----------")
print(sum(max_lst) / len(max_lst))

# Creating MinList by taking two maximum elements from each list

lst1.reverse()
lst2.reverse()
lst3.reverse()

for i in range(0, 2):
    min_lst.append(lst1[i])
    min_lst.append(lst2[i])
    min_lst.append(lst3[i])

min_lst.sort()
print("---------- MinList by taking two elements from each list-----------")
print(min_lst)

# Finding average of minlist
print("---------- Average of Minlist ----------")
print(sum(min_lst) / len(min_lst))








