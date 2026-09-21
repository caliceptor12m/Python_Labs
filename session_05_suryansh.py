# First-run data
product = {'id': 101, 'name': 'Notebook', 'price': 125.0}

# Retrieve using direct key access
product_id = product['id']
product_name = product['name']
product_price = product['price']

print("First Run:")
print("Product Record:", product)
print("ID:", product_id)
print("Name:", product_name)
print("Price:", product_price)

print("\n--- Curated Second Run ---")
product = {'id': 202, 'name': 'Marker', 'price': 45.0}
product_id = product['id']
product_name = product['name']
product_price = product['price']

print("Product Record:", product)
print("ID:", product_id)
print("Name:", product_name)
print("Price:", product_price)




# First-run data
product = {'name': 'Pen', 'price': 20.0}
stock = 50
revised_price = 22.0

print("First Run:")
print("Before update:", product)

# Add a new key and update an existing one
product['stock'] = stock
product['price'] = revised_price

print("After update:", product)

print("\n--- Curated Second Run ---")
product = {'name': 'Pen', 'price': 20.0}
stock = 0
revised_price = 20.0

print("Before update:", product)
product['stock'] = stock
product['price'] = revised_price
print("After update:", product)



# First-run data
employee = {'id': 'E101', 'name': 'Ravi'}
requested_key = 'department'

print("First Run:")
print("Initial employee record:", employee)

# Safely retrieve a key that might be missing
department_value = employee.get(requested_key, 'Not available')

print(f"Requested '{requested_key}':", department_value)

print("\n--- Curated Second Run ---")
employee = {'id': 'E101', 'name': 'Ravi', 'department': 'Finance'}
requested_key = 'department'

print("Initial employee record:", employee)

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
student = {'name': 'Asha', 'marks': {'Python': 82, 'Statistics': 76}}

print("First Run:")
print("Student Record:", student)

# Retrieve values using chained indexing
python_marks = student['marks']['Python']
statistics_marks = student['marks']['Statistics']

print("Python Marks:", python_marks)
print("Statistics Marks:", statistics_marks)

print("\n--- Curated Second Run ---")
student = {'name': 'Asha', 'marks': {'Python': 0, 'Statistics': 100}}

print("Student Record:", student)

python_marks = student['marks']['Python']
statistics_marks = student['marks']['Statistics']

print("Python Marks:", python_marks)
print("Statistics Marks:", statistics_marks)



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

print("First Run:")

# Create an alias and a true copy
alias = original
copied = original.copy()

# Mutate the original dictionary
original['theme'] = 'dark'

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