# First-run data
values = [10, 20, 30, 40, 50]

# Unpack using the asterisk to capture the middle elements
first, *middle, last = values

print("First Run:")
print("Original values:", values)
print("first:", first)
print("middle:", middle)
print("last:", last)

print("\n--- Curated Second Run ---")
values = [10, 50]
first, *middle, last = values
print("Original values:", values)
print("first:", first)
print("middle:", middle)
print("last:", last)




# First-run data
first = [1, 2]
second = [1, 2]

# Create an alias pointing to the exact same object in memory
alias = first

print("First Run:")
print("first == second (Equality):", first == second)
print("first is second (Identity):", first is second)
print("first is alias (Identity):", first is alias)

print("\n--- Curated Second Run ---")
first = []
second = []
alias = first
print("first == second (Equality):", first == second)
print("first is second (Identity):", first is second)
print("first is alias (Identity):", first is alias)




# First-run data
a = 'North'
b = 'South'
c = 'East'

print("First Run:")
print("Before swap -> a:", a, "| b:", b, "| c:", c)

# Swap variables simultaneously using unpacking
a, b, c = b, c, a

print("After swap  -> a:", a, "| b:", b, "| c:", c)

print("\n--- Curated Second Run ---")
a = 'North'
b = 'North'
c = 'East'

print("Before swap -> a:", a, "| b:", b, "| c:", c)
a, b, c = b, c, a
print("After swap  -> a:", a, "| b:", b, "| c:", c)





# First-run data
first = []
second = []

# Mutate the first list to prove they are independent
first.append(1)

print("First Run:")
print("first list:", first)
print("second list:", second)

print("\n--- Curated Second Run ---")
first = ['existing']
second = []

first.append(1)

print("first list:", first)
print("second list:", second)




# First-run data
values = [10, 20]
extra_values = [30, 40]

print("First Run:")
print("Before augmented assignment:", values)

# Update the list in-place using augmented assignment
values += extra_values

print("After augmented assignment:", values)

print("\n--- Curated Second Run ---")
values = []
extra_values = [30, 40]

print("Before augmented assignment:", values)
values += extra_values
print("After augmented assignment:", values)




# First-run data
numbers = [3, 8, 12]

print("First Run:")
print("Numbers list:", numbers)

# Capture max value with walrus operator and evaluate it
is_greater_than_ten = (largest := max(numbers)) > 10

print("Largest computed value:", largest)
print("Is largest > 10?:", is_greater_than_ten)

print("\n--- Curated Second Run ---")
numbers = [-8, -3, -12]

print("Numbers list:", numbers)

is_greater_than_ten = (largest := max(numbers)) > 10

print("Largest computed value:", largest)
print("Is largest > 10?:", is_greater_than_ten)




# First-run data
record = ('E101', ('Asha', 82))

print("First Run:")
print("Original record:", record)

# Unpack the nested tuple structure
employee_id, (employee_name, employee_score) = record

print("Employee ID:", employee_id)
print("Name:", employee_name)
print("Score:", employee_score)

print("\n--- Curated Second Run ---")
record = ('E202', ('Ravi', 0))

print("Original record:", record)

employee_id, (employee_name, employee_score) = record

print("Employee ID:", employee_id)
print("Name:", employee_name)
print("Score:", employee_score)




# First-run data
valid_name = 'total_marks'
value = 240

print("First Run:")
# Invalid assignment target commented out:
# 'total_marks' = value  
# (A literal string cannot be an assignment target because it is an immutable value, not a memory location)

# Correct assignment
valid_name = value
print("Variable 'valid_name' successfully updated to:", valid_name)

print("\n--- Curated Second Run ---")
valid_name = 'score'
value = 0

# 'score' = value  # Invalid literal assignment
valid_name = value
print("Variable 'valid_name' successfully updated to:", valid_name)




