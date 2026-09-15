# First-run data
dividend = 137
divisor = 60

# Calculate quotient and remainder
quotient = dividend // divisor
remainder = dividend % divisor

print("First Run:")
print("Dividend:", dividend, "| Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)

print("\n--- Curated Second Run ---")
dividend = 140
divisor = 60
quotient = dividend // divisor
remainder = dividend % divisor
print("Dividend:", dividend, "| Divisor:", divisor)
print("Quotient:", quotient)
print("Remainder:", remainder)


# First-run data
measurement = 18.3764

# Round to two decimal places
rounded_measurement = round(measurement, 2)

print("First Run:")
print("Original Measurement:", measurement)
print("Rounded Measurement:", rounded_measurement)

print("\n--- Curated Second Run ---")
measurement = 18.375
rounded_measurement = round(measurement, 2)
print("Original Measurement:", measurement)
print("Rounded Measurement:", rounded_measurement)


# First-run data
rupees = 125.75

# Convert to paise and round to a whole number
raw_paise = rupees * 100
exact_paise = round(raw_paise)

print("First Run:")
print("Starting Rupees:", rupees)
print("Raw Paise Calculation:", raw_paise)
print("Exact Paise:", exact_paise)

print("\n--- Curated Second Run ---")
rupees = 0.01
raw_paise = rupees * 100
exact_paise = round(raw_paise)
print("Starting Rupees:", rupees)
print("Raw Paise Calculation:", raw_paise)
print("Exact Paise:", exact_paise)



# First-run data
principal = 50000.0
annual_rate = 0.08
years = 2

# Calculate final amount and growth
final_amount = principal * (1 + annual_rate) ** years
growth_amount = final_amount - principal

print("First Run:")
print("Principal:", principal, "| Annual Rate:", annual_rate, "| Years:", years)
print("Final Amount:", final_amount)
print("Growth Amount:", growth_amount)

print("\n--- Curated Second Run ---")
principal = 50000.0
annual_rate = 0.0
years = 2
final_amount = principal * (1 + annual_rate) ** years
growth_amount = final_amount - principal
print("Principal:", principal, "| Annual Rate:", annual_rate, "| Years:", years)
print("Final Amount:", final_amount)
print("Growth Amount:", growth_amount)



# First-run data
point_a = 18.5
point_b = 42.75

# Calculate absolute distance
distance = abs(point_b - point_a)

print("First Run:")
print("Point A:", point_a, "| Point B:", point_b)
print("Distance:", distance)

print("\n--- Curated Second Run ---")
point_a = 42.75
point_b = 18.5
distance = abs(point_b - point_a)
print("Point A:", point_a, "| Point B:", point_b)
print("Distance:", distance)



# First-run data
number = 45

# Evaluate divisibility
divisible_by_3 = (number % 3) == 0
divisible_by_5 = (number % 5) == 0

print("First Run:")
print("Number to test:", number)
print("Is divisible by 3?", divisible_by_3)
print("Is divisible by 5?", divisible_by_5)

print("\n--- Curated Second Run ---")
number = 9
divisible_by_3 = (number % 3) == 0
divisible_by_5 = (number % 5) == 0
print("Number to test:", number)
print("Is divisible by 3?", divisible_by_3)
print("Is divisible by 5?", divisible_by_5)



# First-run data
byte_count = 5242880

# Convert to KB and MB
kilobytes = byte_count / 1024
megabytes = kilobytes / 1024

print("First Run:")
print("Starting Bytes:", byte_count)
print("Kilobytes (KB):", kilobytes)
print("Megabytes (MB):", megabytes)

print("\n--- Curated Second Run ---")
byte_count = 1024
kilobytes = byte_count / 1024
megabytes = kilobytes / 1024
print("Starting Bytes:", byte_count)
print("Kilobytes (KB):", kilobytes)
print("Megabytes (MB):", megabytes)




# First-run data
x = 4
a = 2
b = 3
c = 5

# Calculate individual terms
squared_term = a * (x ** 2)
linear_term = b * x

# Calculate final polynomial value
polynomial_value = squared_term + linear_term + c

print("First Run:")
print("Inputs: x=", x, "| a=", a, "| b=", b, "| c=", c)
print("Squared Term:", squared_term)
print("Linear Term:", linear_term)
print("Final Polynomial Value:", polynomial_value)

print("\n--- Curated Second Run ---")
x = 0
a = 2
b = 3
c = 5
squared_term = a * (x ** 2)
linear_term = b * x
polynomial_value = squared_term + linear_term + c
print("Inputs: x=", x, "| a=", a, "| b=", b, "| c=", c)
print("Squared Term:", squared_term)
print("Linear Term:", linear_term)
print("Final Polynomial Value:", polynomial_value)



