list1 = [9, 3, 6, 4, 3, 6, 7, 6]
for each_num in list1:
  if list1.count(each_num) > 1:
    list1.remove(each_num)
print(list1)