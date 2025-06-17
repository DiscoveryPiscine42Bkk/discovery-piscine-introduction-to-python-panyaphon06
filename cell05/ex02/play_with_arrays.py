my_array = [2, 8, 9, 48, 8, 22, -12, 2]

new_array = [x + 2 for x in my_array]

print("Original array:", my_array)
print("New array:", [x for x in new_array if x > 5])

