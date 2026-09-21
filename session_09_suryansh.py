# First-run data
n = 10
total = 0

print("First Run:")
print("Summing integers up to:", n)

# For loop with an accumulator
for i in range(1, n + 1):
    total += i
    print(f"Added {i}, running total is now {total}")

print("Final Total:", total)

print("\n--- Curated Second Run ---")
n = 0
total = 0

print("Summing integers up to:", n)

for i in range(1, n + 1):
    total += i
    print(f"Added {i}, running total is now {total}")

print("Final Total:", total)




# First-run data
number = 7

print("First Run:")
print(f"Multiplication table for {number}:")

# Loop 10 times to generate table rows
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")

print("\n--- Curated Second Run ---")
number = 0

print(f"Multiplication table for {number}:")

for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")




    # First-run data
number = 6
factorial = 1

print("First Run:")
print(f"Computing factorial of {number}:")

# Iteratively multiply the accumulator
for i in range(1, number + 1):
    factorial *= i
    print(f"Iteration {i}: running factorial is {factorial}")

print("Final Factorial:", factorial)

print("\n--- Curated Second Run ---")
number = 0
factorial = 1

print(f"Computing factorial of {number}:")

for i in range(1, number + 1):
    factorial *= i
    print(f"Iteration {i}: running factorial is {factorial}")

print("Final Factorial:", factorial)




# First-run data
number = 50842
working_number = number
iterations = 0

print("First Run:")
print("Starting number:", number)

# Repeatedly apply floor division by 10 to count digits
while working_number > 0:
    working_number //= 10
    iterations += 1

print("Total digits (iterations):", iterations)

print("\n--- Curated Second Run ---")
number = 7
working_number = number
iterations = 0

print("Starting number:", number)

while working_number > 0:
    working_number //= 10
    iterations += 1

print("Total digits (iterations):", iterations)



# First-run data
values = [12, 7, 18, 5, 21]
target = 18
found_value = None

print("First Run:")
print(f"Target: {target}")

# Loop and break when target is found
for value in values:
    if value == target:
        found_value = value
        break

print("Found value:", found_value)

print("\n--- Curated Second Run ---")
values = [12, 7, 18, 5, 21]
target = 99
found_value = None

print(f"Target: {target}")

for value in values:
    if value == target:
        found_value = value
        break

print("Found value:", found_value)




# First-run data
entries = ['12', '7', '5', 'done']
total = 0

print("First Run:")
print("Entries list:", entries)

# Break on sentinel value, otherwise add to total
for entry in entries:
    if entry == 'done':
        print("Sentinel 'done' reached. Breaking loop.")
        break
    total += int(entry)

print("Total sum:", total)

print("\n--- Curated Second Run ---")
entries = ['done']
total = 0

print("Entries list:", entries)

for entry in entries:
    if entry == 'done':
        print("Sentinel 'done' reached. Breaking loop.")
        break
    total += int(entry)

print("Total sum:", total)




# First-run data
rows = 5

print("First Run:")
print(f"Triangle with {rows} rows:")

# Use a loop with string repetition to print the triangle
for i in range(1, rows + 1):
    print('*' * i)

print("\n--- Curated Second Run ---")
rows = 1

print(f"Triangle with {rows} rows:")

for i in range(1, rows + 1):
    print('*' * i)




    # First-run data
number = 29
is_prime = True

print("First Run:")
print(f"Testing primality of {number}...")

# Test possible divisors from 2 up to number - 1
for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

print("Is prime?:", is_prime)

print("\n--- Curated Second Run ---")
number = 2
is_prime = True

print(f"Testing primality of {number}...")

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

print("Is prime?:", is_prime)