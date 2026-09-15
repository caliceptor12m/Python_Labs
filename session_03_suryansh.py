# First-run data
text = 'Data Science'

# Normalize to lowercase and count each vowel
lower_text = text.lower()
vowel_count = (lower_text.count('a') + lower_text.count('e') + 
               lower_text.count('i') + lower_text.count('o') + 
               lower_text.count('u'))

print("First Run:")
print("Original Text:", text)
print("Normalized Text:", lower_text)
print("Total Vowels:", vowel_count)

print("\n--- Curated Second Run ---")
text = 'AEIOU'
lower_text = text.lower()
vowel_count = (lower_text.count('a') + lower_text.count('e') + 
               lower_text.count('i') + lower_text.count('o') + 
               lower_text.count('u'))
print("Original Text:", text)
print("Normalized Text:", lower_text)
print("Total Vowels:", vowel_count)



#first -run data 
text = 'python'
# reverse string using slicing
reversed_text = text[::-1]
print("First Run:")
print("Original String:", text)
print("Reversed String:", reversed_text)

print("\n--- Curated Second Run ---")
text = ''
reversed_text = text[::-1]
print("Original String:", repr(text))
print("Reversed String:", repr(reversed_text))




# First-run data
text = '  Never Odd Or Even  '

# Normalize string and test against its reverse
normalized_text = text.strip().lower().replace(' ', '')
reversed_normalized = normalized_text[::-1]
is_palindrome = (normalized_text == reversed_normalized)

print("First Run:")
print("Original Text:", text)
print("Normalized Text:", normalized_text)
print("Is Palindrome?:", is_palindrome)

print("\n--- Curated Second Run ---")
text = 'Python'
normalized_text = text.strip().lower().replace(' ', '')
reversed_normalized = normalized_text[::-1]
is_palindrome = (normalized_text == reversed_normalized)
print("Original Text:", text)
print("Normalized Text:", normalized_text)
print("Is Palindrome?:", is_palindrome)



# First-run data
filename = 'quarterly_report.csv'

# Split from the right exactly once
split_parts = filename.rsplit('.', 1)
extension = split_parts[1]

print("First Run:")
print("Original Filename:", filename)
print("Split Parts:", split_parts)
print("Final Extension:", extension)

print("\n--- Curated Second Run ---")
filename = 'archive.tar.gz'
split_parts = filename.rsplit('.', 1)
extension = split_parts[1]
print("Original Filename:", filename)
print("Split Parts:", split_parts)
print("Final Extension:", extension)



# First-run data (contains exactly 3 spaces between words)
text = 'Python   makes   text   readable'

# Replace 3 spaces with 1 space
cleaned_text = text.replace('   ', ' ')

print("First Run:")
print("Original Text:", text)
print("Cleaned Text:", cleaned_text)

print("\n--- Curated Second Run ---")
text = 'Already single spaced'
cleaned_text = text.replace('   ', ' ')
print("Original Text:", text)
print("Cleaned Text:", cleaned_text)



# First-run data
full_name = 'Asha Mehta Singh'

# Split into parts and manually concatenate the initials
parts = full_name.split()
initials = parts[0][0] + '.' + parts[1][0] + '.' + parts[2][0] + '.'

print("First Run:")
print("Full Name:", full_name)
print("Split Parts:", parts)
print("Initials:", initials)

print("\n--- Curated Second Run ---")
full_name = 'Ravi Kumar Shah'
parts = full_name.split()
initials = parts[0][0] + '.' + parts[1][0] + '.' + parts[2][0] + '.'
print("Full Name:", full_name)
print("Split Parts:", parts)
print("Initials:", initials)



# First-run data
sentence = 'data helps data teams'
target = 'data'

# Count occurrences exactly
occurrence_count = sentence.count(target)

print("First Run:")
print("Sentence:", sentence)
print("Target Word:", target)
print("Occurrences:", occurrence_count)

print("\n--- Curated Second Run ---")
sentence = 'Data helps data teams'
target = 'data'
occurrence_count = sentence.count(target)
print("Sentence:", sentence)
print("Target Word:", target)
print("Occurrences:", occurrence_count)



# First-run data
item = 'Notebook'
quantity = 3
unit_price = 125.5

# Calculate total and format receipt line
line_total = quantity * unit_price
receipt_line = f"Item: {item} | Qty: {quantity} | Price: {unit_price:.2f} | Total: {line_total:.2f}"

print("First Run:")
print(receipt_line)

print("\n--- Curated Second Run ---")
item = 'Notebook'
quantity = 0
unit_price = 125.5
line_total = quantity * unit_price
receipt_line = f"Item: {item} | Qty: {quantity} | Price: {unit_price:.2f} | Total: {line_total:.2f}"
print(receipt_line)