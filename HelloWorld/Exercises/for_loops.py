numbers = [5, 2, 5, 2, 2]

for x_count in numbers:
    output = ""
    for num in range(x_count):
        output += "x"
    print(output)

print()


list1 = [9, 6, 9, 9, 4, 4, 3, 6, 7, 6]
list1.sort()
for each_num in list1:
    if list1.count(each_num) > 1:
        list1.remove(each_num)
print(list1)
