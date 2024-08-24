"""Make your own list. Print the largest value present in the list"""

my_list = [2, 3, -4, 5, 66, -10]
largest = my_list[0]

for i in range(0, len(my_list)):
    # print(my_list[i], end=" ")
    if my_list[i] > largest:
        largest = my_list[i]

print(f"largest: {largest}")

smallest = my_list[0]
for i in range(0, len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]

print(f"smallest: {smallest}")
