# First-run data
dividend = 137
divisor = 60

# Calculate using floor division and modulo
quotient = dividend // divisor
remainder = dividend % divisor

# Store in a tuple and unpack it
result = (quotient, remainder)
unpacked_quotient, unpacked_remainder = result

print("First Run:")
print(f"Dividing {dividend} by {divisor}")
print("Result Tuple:", result)
print("Unpacked Quotient:", unpacked_quotient)
print("Unpacked Remainder:", unpacked_remainder)

print("\n--- Curated Second Run ---")
dividend = 5
divisor = 8

quotient = dividend // divisor
remainder = dividend % divisor

result = (quotient, remainder)
unpacked_quotient, unpacked_remainder = result

print(f"Dividing {dividend} by {divisor}")
print("Result Tuple:", result)
print("Unpacked Quotient:", unpacked_quotient)
print("Unpacked Remainder:", unpacked_remainder)



from pathlib import Path

# First-run data
path_text = 'North\nSouth\nEast\n'

# Create Path, write, read, and delete
temp_file = Path('temp_file.txt')
temp_file.write_text(path_text, encoding='utf-8')
read_content = temp_file.read_text(encoding='utf-8')

print("First Run:")
print("Original string passed:", repr(path_text))
print("String read from file:", repr(read_content))

# Clean up
temp_file.unlink()

print("\n--- Curated Second Run ---")
path_text = ''
temp_file.write_text(path_text, encoding='utf-8')
read_content = temp_file.read_text(encoding='utf-8')

print("Original string passed:", repr(path_text))
print("String read from file:", repr(read_content))

temp_file.unlink()



from pathlib import Path

# First-run data
source_text = 'Python files are readable.'

# Define both file paths
file1 = Path('source.txt')
file2 = Path('upper.txt')

# Write, read, transform, and write to second file
file1.write_text(source_text, encoding='utf-8')
content = file1.read_text(encoding='utf-8')

upper_content = content.upper()
file2.write_text(upper_content, encoding='utf-8')

# Verify and delete
verified_text = file2.read_text(encoding='utf-8')

print("First Run:")
print("Original text:", source_text)
print("Verified uppercase text:", verified_text)

file1.unlink()
file2.unlink()

print("\n--- Curated Second Run ---")
source_text = 'Mixed Case 123.'

file1.write_text(source_text, encoding='utf-8')
content = file1.read_text(encoding='utf-8')

upper_content = content.upper()
file2.write_text(upper_content, encoding='utf-8')

verified_text = file2.read_text(encoding='utf-8')

print("Original text:", source_text)
print("Verified uppercase text:", verified_text)

file1.unlink()
file2.unlink()