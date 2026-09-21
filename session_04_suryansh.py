# First-run data
products = ['Pen', 'Notebook', 'Marker', 'Folder', 'Stapler']

print("First Run:")
print("Original list:", products)
print("products[0] (First item):", products[0])
print("products[-1] (Last item):", products[-1])
print("products[1:4] (Middle slice):", products[1:4])
print("products[::-1] (Reversed):", products[::-1])

print("\n--- Curated Second Run ---")
products = ['Only item']
print("Original list:", products)
print("products[0] (First item):", products[0])
print("products[-1] (Last item):", products[-1])
print("products[1:4] (Middle slice):", products[1:4])
print("products[::-1] (Reversed):", products[::-1])




# First-run data
items = ['Pen', 'Notebook']
new_items = ['Marker', 'Folder']

# Make copies so we can test both methods independently
items_for_append = items.copy()
items_for_extend = items.copy()

# Apply the methods
items_for_append.append(new_items)
items_for_extend.extend(new_items)

print("First Run:")
print("Appended list:", items_for_append)
print("Extended list:", items_for_extend)

print("\n--- Curated Second Run ---")
items = []
new_items = ['Marker', 'Folder']

items_for_append = items.copy()
items_for_extend = items.copy()

items_for_append.append(new_items)
items_for_extend.extend(new_items)

print("Appended list:", items_for_append)
print("Extended list:", items_for_extend)




# First-run data
cities = ['Delhi', 'Mumbai', 'Pune', 'Jaipur']
removed_city = 'Pune'

print("First Run:")
print("Initial cities:", cities)
cities.insert(1, 'Chennai')
print("After insert:", cities)
cities.remove(removed_city)
print("After remove:", cities)
popped_city = cities.pop()
print("After pop:", cities)
print("Popped city:", popped_city)

print("\n--- Curated Second Run ---")
cities = ['Delhi', 'Pune']
removed_city = 'Pune'
print("Initial cities:", cities)
cities.insert(1, 'Chennai')
print("After insert:", cities)
cities.remove(removed_city)
print("After remove:", cities)
popped_city = cities.pop()
print("After pop:", cities)
print("Popped city:", popped_city)



# First-run data
scores = [72, 91, 68, 85, 77]

# Create a sorted copy without modifying the original
sorted_scores = sorted(scores)

# Sort the original list in-place, in reverse order
scores.sort(reverse=True)

print("First Run:")
print("sorted_scores (ascending copy):", sorted_scores)
print("scores (modified in-place, descending):", scores)

print("\n--- Curated Second Run ---")
scores = [85, 85, 72]
sorted_scores = sorted(scores)
scores.sort(reverse=True)
print("sorted_scores (ascending copy):", sorted_scores)
print("scores (modified in-place, descending):", scores)



# First-run data
matrix = [[10, 20], [30, 40], [50, 60]]

# Retrieve values using two indexes (first for row, second for item)
value_10 = matrix[0][0]
value_40 = matrix[1][1]
value_60 = matrix[2][1]

print("First Run:")
print("Matrix:", matrix)
print("Retrieved 10 (row 0, item 0):", value_10)
print("Retrieved 40 (row 1, item 1):", value_40)
print("Retrieved 60 (row 2, item 1):", value_60)

print("\n--- Curated Second Run ---")
matrix = [[1, 2], [3, 4], [5, 6]]
value_10 = matrix[0][0]
value_40 = matrix[1][1]
value_60 = matrix[2][1]
print("Matrix:", matrix)
print("Retrieved first target (row 0, item 0):", value_10)
print("Retrieved second target (row 1, item 1):", value_40)
print("Retrieved third target (row 2, item 1):", value_60)



# First-run data
original = [10, 20, 30]

# Create an alias (both variables reference the same list in memory)
alias = original
alias.append(40)

print("First Run:")
print("Alias list:", alias)
print("Original list:", original)

print("\n--- Curated Second Run ---")
original = []
alias = original
alias.append(40)
print("Alias list:", alias)
print("Original list:", original)



# First-run data
original = [[1], [2]]

# Make an explicit independent copy of each nested list
independent = [original[0].copy(), original[1].copy()]

# Mutate the original to prove they are independent
original[0].append(99)

print("First Run:")
print("Original list (mutated):", original)
print("Independent copy (unchanged):", independent)

print("\n--- Curated Second Run ---")
original = [[], []]
independent = [original[0].copy(), original[1].copy()]
original[0].append(99)
print("Original list (mutated):", original)
print("Independent copy (unchanged):", independent)



# First-run data
first_list = ['A', 'B']
second_list = ['C', 'D']
repeat_count = 2

# Combine and repeat using mathematical operators
combined = first_list + second_list
repeated = combined * repeat_count

print("First Run:")
print("Combined list:", combined)
print("Repeated list:", repeated)

print("\n--- Curated Second Run ---")
first_list = ['A']
second_list = []
repeat_count = 0
combined = first_list + second_list
repeated = combined * repeat_count
print("Combined list:", combined)
print("Repeated list:", repeated)




# First-run data
employee = {'id': 'E101', 'name': 'Ravi'}
requested_key = 'department'

print("First Run:")
print("Employee Record:", employee)
# Use get() to safely handle missing keys
department_value = employee.get(requested_key, 'Not available')
print(f"Requested '{requested_key}':", department_value)

print("\n--- Curated Second Run ---")
employee = {'id': 'E101', 'name': 'Ravi', 'department': 'Finance'}
requested_key = 'department'
print("Employee Record:", employee)
department_value = employee.get(requested_key, 'Not available')
print(f"Requested '{requested_key}':", department_value)



# First-run data
cart = {'Pen': 3, 'Notebook': 2, 'Marker': 1}
item_to_remove = 'Marker'

print("First Run:")
print("Initial cart:", cart)
# Remove the key-value pair and store the value
removed_quantity = cart.pop(item_to_remove)
print("Removed quantity:", removed_quantity)
print("Remaining cart:", cart)

print("\n--- Curated Second Run ---")
cart = {'Pen': 3, 'Notebook': 2}
item_to_remove = 'Pen'
print("Initial cart:", cart)
removed_quantity = cart.pop(item_to_remove)
print("Removed quantity:", removed_quantity)
print("Remaining cart:", cart)



# First-run data
defaults = {'theme': 'light', 'page_size': 20}
user = {'theme': 'dark'}

print("First Run:")
print("Defaults:", defaults)
print("User prefs:", user)
# Merge using the union operator (|)
settings = defaults | user
print("Merged Settings:", settings)

print("\n--- Curated Second Run ---")
defaults = {'theme': 'light', 'page_size': 20}
user = {'page_size': 50}
print("Defaults:", defaults)
print("User prefs:", user)
settings = defaults | user
print("Merged Settings:", settings)




# First-run data
inventory = {'Pen': 40, 'Notebook': 25, 'Marker': 18}

print("First Run:")
print("Inventory:", inventory)
# Create views
keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()

print("Keys View:", keys_view)
print("Values View:", values_view)
print("Items View:", items_view)

print("\n--- Curated Second Run ---")
inventory = {}
print("Inventory:", inventory)
keys_view = inventory.keys()
values_view = inventory.values()
items_view = inventory.items()
print("Keys View:", keys_view)
print("Values View:", values_view)
print("Items View:", items_view)



# First-run data
original = {'theme': 'light', 'page_size': 20}

# Create an alias and a true copy
alias = original
copied = original.copy()

# Mutate the original dictionary
original['theme'] = 'dark'

print("First Run:")
print("Original dictionary:", original)
print("Alias dictionary:", alias)
print("Copied dictionary:", copied)

print("\n--- Curated Second Run ---")
original = {}
alias = original
copied = original.copy()
original['theme'] = 'dark'
print("Original dictionary:", original)
print("Alias dictionary:", alias)
print("Copied dictionary:", copied)



