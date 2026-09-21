# First-run data
celsius = 32.0

# Calculate Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Output results
print("First Run:")
print("Starting Celsius:", celsius)
print("Resulting Fahrenheit:", fahrenheit)

print("\n--- Curated Second Run ---")
celsius = 0.0
fahrenheit = (celsius * 9 / 5) + 32
print("Starting Celsius:", celsius)
print("Resulting Fahrenheit:", fahrenheit)



# First-run data
principal = 25000
rate = 6.5
time_years = 3

# Calculate simple interest and final amount
simple_interest = principal * rate * time_years / 100
final_amount = principal + simple_interest

print("First Run:")
print("Principal:", principal, "Rate:", rate, "Time:", time_years)
print("Simple Interest:", simple_interest)
print("Final Amount:", final_amount)

print("\n--- Curated Second Run ---")
principal = 0
rate = 6.5
time_years = 3
simple_interest = principal * rate * time_years / 100
final_amount = principal + simple_interest
print("Principal:", principal, "Rate:", rate, "Time:", time_years)
print("Simple Interest:", simple_interest)
print("Final Amount:", final_amount)



# First-run data
first_number = 48
second_number = 35
# Evaluate comparison
first_is_greater = first_number > second_number
print("First Run:")
print("First Number:", first_number)
print("Second Number:", second_number)
print("Is First Greater?:", first_is_greater)

print("\n--- Curated Second Run ---")
first_number = 35
second_number = 35
first_is_greater = first_number > second_number
print("First Number:", first_number)
print("Second Number:", second_number)
print("Is First Greater?:", first_is_greater)



# First-run data
mark_1 = 72
mark_2 = 81
mark_3 = 69

# Calculate total and average
total_marks = mark_1 + mark_2 + mark_3
average_marks = total_marks / 3

print("First Run:")
print("Marks:", mark_1, mark_2, mark_3)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print("\n--- Curated Second Run ---")
mark_1 = 0
mark_2 = 0
mark_3 = 0
total_marks = mark_1 + mark_2 + mark_3
average_marks = total_marks / 3
print("Marks:", mark_1, mark_2, mark_3)
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)


# First-run data
total_seconds = 7384

# Convert to hours, minutes, seconds using // and %
hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60

print("First Run:")
print("Total Seconds:", total_seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)

print("\n--- Curated Second Run ---")
total_seconds = 59
hours = total_seconds // 3600
remaining_after_hours = total_seconds % 3600
minutes = remaining_after_hours // 60
seconds = remaining_after_hours % 60
print("Total Seconds:", total_seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)



# First-run data
price = 2400.0
discount_rate = 0.15

# Calculate discount and final price
discount_amount = price * discount_rate
final_price = price - discount_amount

print("First Run:")
print("Starting Price:", price, "| Discount Rate:", discount_rate)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)

print("\n--- Curated Second Run ---")
price = 2400.0
discount_rate = 0.0
discount_amount = price * discount_rate
final_price = price - discount_amount
print("Starting Price:", price, "| Discount Rate:", discount_rate)
print("Discount Amount:", discount_amount)
print("Final Price:", final_price)



# First-run data
first_value = 12
second_value = 45

print("First Run:")
print("Before Swap -> First:", first_value, "| Second:", second_value)

# Simultaneous swap
first_value, second_value = second_value, first_value
print("After Swap  -> First:", first_value, "| Second:", second_value)

print("\n--- Curated Second Run ---")
first_value = 12
second_value = 12
print("Before Swap -> First:", first_value, "| Second:", second_value)
first_value, second_value = second_value, first_value
print("After Swap  -> First:", first_value, "| Second:", second_value)



# First-run data
a = 8
b = 3
c = 2

# Enforce order of operations
multiplication_result = b * c
final_result = a + multiplication_result

print("First Run:")
print("Inputs: a=", a, "b=", b, "c=", c)
print("Intermediate Multiplication:", multiplication_result)
print("Final Result:", final_result)

print("\n--- Curated Second Run ---")
a = 9
b = 3
c = 2
multiplication_result = b * c
final_result = a + multiplication_result
print("Inputs: a=", a, "b=", b, "c=", c)
print("Intermediate Multiplication:", multiplication_result)
print("Final Result:", final_result)


# First-run data
product = {'id': 101, 'name': 'Notebook', 'price': 125.0}

# Retrieve using direct key access
product_id = product['id']
product_name = product['name']
product_price = product['price']

print("First Run:")
print("Product Dictionary:", product)
print("ID:", product_id)
print("Name:", product_name)
print("Price:", product_price)

print("\n--- Curated Second Run ---")
product = {'id': 202, 'name': 'Marker', 'price': 45.0}
product_id = product['id']
product_name = product['name']
product_price = product['price']
print("Product Dictionary:", product)
print("ID:", product_id)
print("Name:", product_name)
print("Price:", product_price)



# First-run data
product = {'name': 'Pen', 'price': 20.0}
stock = 50
revised_price = 22.0

print("First Run:")
print("Original Dictionary:", product)
# Add new key and update existing key
product['stock'] = stock
product['price'] = revised_price
print("Updated Dictionary:", product)

print("\n--- Curated Second Run ---")
product = {'name': 'Pen', 'price': 20.0}
stock = 0
revised_price = 20.0
print("Original Dictionary:", product)
product['stock'] = stock
product['price'] = revised_price
print("Updated Dictionary:", product)