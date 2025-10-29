# Get input from user
num = int(input("Enter a number: "))

# Start with factorial = 1
factorial = 1

# Multiply all numbers from 1 to num
for i in range(1, num + 1):
    factorial = factorial * i

# Result
print("Factorial is", factorial)