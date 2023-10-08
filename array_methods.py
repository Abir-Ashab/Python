places = ["Dhaka", "Ctg", "comilla", "B-baria", "sylhet"]

# len function
print(len(places))

# index func
print(places.index("Ctg"))

# append func
places.append("khulna")
print(places)

# insert
places.insert(2, "barishal")
print(places)

# remove
places.remove("barishal")
print(places)

# sort-ascending(big letter first, then smaller letters)
places.sort()
print(places)

# alphabetical order
places.sort(key = str.lower)
print(places)

# alphabetical order(reverse)
places.sort(key = str.lower, reverse=True)
print(places)










# Given by gpt



# Create a list
my_list = [1, 2, 3, 4, 5]

# Access elements by index
print("Element at index 2:", my_list[2])

# Modify elements by index
my_list[3] = 99
print("Modified list:", my_list)

# Append an element to the end of the list
my_list.append(6)
print("After appending 6:", my_list)

# Insert an element at a specific index
my_list.insert(1, 7)
print("After inserting 7 at index 1:", my_list)

# Remove an element by value
my_list.remove(3)
print("After removing 3:", my_list)

# Remove an element by index
popped_element = my_list.pop(4)
print("Popped element at index 4:", popped_element)
print("List after popping:", my_list)

# Find the index of an element
index = my_list.index(1)
print("Index of 4:", index)

# Count the occurrences of an element
count = my_list.count(7)
print("Count of 7:", count)

# Sort the list in ascending order
my_list.sort()
print("Sorted list:", my_list)

# Reverse the list in-place
my_list.reverse()
print("Reversed list:", my_list)

# Create a copy of the list
copy_of_list = my_list.copy()
print("Copy of the list:", copy_of_list)

# Checking membership
if not my_list:
    print("The list is empty")

# Checking for the presence of an element
is_present = 3 in my_list  # Returns True if 3 is in the list
print(is_present)


# Nested lists
nested_list = [[1, 2, 3], [4, 5, 6]]

# Length of the list
list_length = len(my_list)

# Min and max values
min_value = min(my_list)
max_value = max(my_list)

# List comprehensions
squared_values = [x ** 2 for x in my_list if x % 2 == 0]

# List concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2


# Zipping lists
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))  # Combines elements from both lists into tuples
print('zipped list', zipped)

# Unzipping lists
unzipped = list(zip(*zipped))  # Unzips the zipped list into separate lists
print('unzipped list', unzipped)

# Clear all elements from the list
my_list.clear()
print("Cleared list:", my_list)