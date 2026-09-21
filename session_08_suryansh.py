# First-run data
number = -7

print("First Run:")
print("Input number:", number)

# Classify using if/elif/else
if number < 0:
    classification = 'negative'
elif number == 0:
    classification = 'zero'
else:
    classification = 'positive'

print("Classification:", classification)

print("\n--- Curated Second Run ---")
number = 0

print("Input number:", number)

if number < 0:
    classification = 'negative'
elif number == 0:
    classification = 'zero'
else:
    classification = 'positive'

print("Classification:", classification)




# First-run data
score = 84

print("First Run:")
print("Input score:", score)

# Validate bounds before assigning a grade
if 0 <= score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Assigned Grade:", grade)
else:
    print("Error: Score out of bounds (must be 0-100).")

print("\n--- Curated Second Run ---")
score = 101

print("Input score:", score)

if 0 <= score <= 100:
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
    print("Assigned Grade:", grade)
else:
    print("Error: Score out of bounds (must be 0-100).")




# First-run data
year = 2028

print("First Run:")
print("Input year:", year)

# Apply Gregorian leap year rule: divisible by 400, OR divisible by 4 but NOT 100
is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

print("Is leap year?:", is_leap_year)

print("\n--- Curated Second Run ---")
year = 1900

print("Input year:", year)

is_leap_year = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

print("Is leap year?:", is_leap_year)




# First-run data
username = 'asha_01'
password = 'Data@123'

print("First Run:")
print("Username:", username, "| Password:", password)

# Evaluate individual conditions
valid_user_len = len(username) >= 6
valid_pass_len = len(password) >= 8
has_at_symbol = '@' in password

# Combine the three named Boolean tests
is_valid = valid_user_len and valid_pass_len and has_at_symbol

print("Valid username length?:", valid_user_len)
print("Valid password length?:", valid_pass_len)
print("Password contains '@'?:", has_at_symbol)
print("Overall Account Valid?:", is_valid)

print("\n--- Curated Second Run ---")
username = 'asha'
password = 'short'

print("Username:", username, "| Password:", password)

valid_user_len = len(username) >= 6
valid_pass_len = len(password) >= 8
has_at_symbol = '@' in password

is_valid = valid_user_len and valid_pass_len and has_at_symbol

print("Valid username length?:", valid_user_len)
print("Valid password length?:", valid_pass_len)
print("Password contains '@'?:", has_at_symbol)
print("Overall Account Valid?:", is_valid)



# First-run data
a = 18
b = 42
c = 27

print("First Run:")
print(f"Values -> a: {a}, b: {b}, c: {c}")

# Find largest using chained conditionals (handling equality)
if a >= b and a >= c:
    largest_value = a
elif b >= a and b >= c:
    largest_value = b
else:
    largest_value = c

print("Largest value:", largest_value)

print("\n--- Curated Second Run ---")
a = 42
b = 42
c = 27

print(f"Values -> a: {a}, b: {b}, c: {c}")

if a >= b and a >= c:
    largest_value = a
elif b >= a and b >= c:
    largest_value = b
else:
    largest_value = c

print("Largest value:", largest_value)




# First-run data
side_1 = 5
side_2 = 5
side_3 = 8

print("First Run:")
print(f"Sides: {side_1}, {side_2}, {side_3}")

# Validate triangle inequality theorem
if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
    # Classify the valid triangle
    if side_1 == side_2 == side_3:
        classification = 'equilateral'
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        classification = 'isosceles'
    else:
        classification = 'scalene'
else:
    classification = 'invalid (violates triangle inequality)'

print("Triangle Classification:", classification)

print("\n--- Curated Second Run ---")
side_1 = 1
side_2 = 2
side_3 = 8

print(f"Sides: {side_1}, {side_2}, {side_3}")

if (side_1 + side_2 > side_3) and (side_1 + side_3 > side_2) and (side_2 + side_3 > side_1):
    if side_1 == side_2 == side_3:
        classification = 'equilateral'
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        classification = 'isosceles'
    else:
        classification = 'scalene'
else:
    classification = 'invalid (violates triangle inequality)'

print("Triangle Classification:", classification)




# First-run data
day_number = 3

print("First Run:")
print("Input day number:", day_number)

# Select a weekday using match-case structural pattern matching
match day_number:
    case 1:
        weekday = 'Monday'
    case 2:
        weekday = 'Tuesday'
    case 3:
        weekday = 'Wednesday'
    case 4:
        weekday = 'Thursday'
    case 5:
        weekday = 'Friday'
    case 6:
        weekday = 'Saturday'
    case 7:
        weekday = 'Sunday'
    case _:
        weekday = 'Invalid day number'

print("Selected weekday:", weekday)

print("\n--- Curated Second Run ---")
day_number = 9

print("Input day number:", day_number)

match day_number:
    case 1:
        weekday = 'Monday'
    case 2:
        weekday = 'Tuesday'
    case 3:
        weekday = 'Wednesday'
    case 4:
        weekday = 'Thursday'
    case 5:
        weekday = 'Friday'
    case 6:
        weekday = 'Saturday'
    case 7:
        weekday = 'Sunday'
    case _:
        weekday = 'Invalid day number'

print("Selected weekday:", weekday)




# First-run data
transaction = ('withdrawal', 25000)

print("First Run:")
print("Transaction Record:", transaction)

# Match transaction records using cases with conditional guards
match transaction:
    case ('deposit', amount) if amount > 0:
        status = f"Accepted deposit of {amount}"
    case ('withdrawal', amount) if amount > 20000:
        status = f"Review required for large withdrawal of {amount}"
    case ('withdrawal', amount) if amount > 0:
        status = f"Accepted withdrawal of {amount}"
    case _:
        status = "Unsupported transaction record"

print("Transaction Status:", status)

print("\n--- Curated Second Run ---")
transaction = ('withdrawal', 5000)

print("Transaction Record:", transaction)

match transaction:
    case ('deposit', amount) if amount > 0:
        status = f"Accepted deposit of {amount}"
    case ('withdrawal', amount) if amount > 20000:
        status = f"Review required for large withdrawal of {amount}"
    case ('withdrawal', amount) if amount > 0:
        status = f"Accepted withdrawal of {amount}"
    case _:
        status = "Unsupported transaction record"

print("Transaction Status:", status)




# First-run data
transaction = ('withdrawal', 25000)

print("First Run:")
print("Transaction Record:", transaction)

# Match transaction records using cases with conditional guards
match transaction:
    case ('deposit', amount) if amount > 0:
        status = f"Accepted deposit of {amount}"
    case ('withdrawal', amount) if amount > 20000:
        status = f"Review required for large withdrawal of {amount}"
    case ('withdrawal', amount) if amount > 0:
        status = f"Accepted withdrawal of {amount}"
    case _:
        status = "Unsupported transaction record"

print("Transaction Status:", status)

print("\n--- Curated Second Run ---")
transaction = ('withdrawal', 5000)

print("Transaction Record:", transaction)

match transaction:
    case ('deposit', amount) if amount > 0:
        status = f"Accepted deposit of {amount}"
    case ('withdrawal', amount) if amount > 20000:
        status = f"Review required for large withdrawal of {amount}"
    case ('withdrawal', amount) if amount > 0:
        status = f"Accepted withdrawal of {amount}"
    case _:
        status = "Unsupported transaction record"

print("Transaction Status:", status)