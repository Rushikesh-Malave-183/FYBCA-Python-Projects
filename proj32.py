my_list = [1, 2, 3, 4, 5, 6]
print("Original list:", my_list)

my_list.extend([7, 8, 9])
print("List after extending:", my_list)

my_list.insert(1, 12)
print("List after inserting:", my_list)

my_list.remove(5)
print("List after removing:", my_list)

print("Index of 9:", my_list.index(9))

my_list.reverse()
print("List after reversing:", my_list)

copied_list = my_list.copy()
print("Copied list:", copied_list)

copied_list.clear()
print("List after clearing:", copied_list)
