# Program to print first N Fibonacci numbers
# Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...

# Get input from user
n = int(input("Enter number of terms: "))

# First two numbers
a = 0
b = 1

# Print first n fibonacci numbers
for i in range(n):
    print(a, end=" ")
    # Calculate next number
    next_num = a + b
    a = b
    b = next_num