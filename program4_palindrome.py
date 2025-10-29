# Program to check if a string is palindrome
# Examples: racecar, madam, level, noon, mom, dad, radar

# Get input from user
text = input("Enter a string: ")

# Convert to lowercase for comparison
text = text.lower()

# Check if string is same as its reverse
if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")