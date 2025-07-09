# Print Function
print("Hello, World!")

# String Manipulation
# Possible Error: IndentationError or SyntaxError
print("Hello, World!\nGood Bye, World!")
print("Hello," + " " + "David!")

# Improved: Using String Format
print(f"Hello, {"David!"}")

# Input Function
# Single Liner
print("Hello, " + input("Hello, what is your name?\nName: ") + "!")

# Variables
# Possible Error: SyntaxError, NameError, TypeError
myPhoneNumber = "09123456789" # Don"t use int if it"s start with 0 value, Use string
print(f"This is my Phone Number: {myPhoneNumber}")
myPhoneNumber = "09987654321"
print(f"This is my Phone Number: {myPhoneNumber}") # Output: 09987654321
print(f"Length of Phone Number: {len(myPhoneNumber)}")
age = 23
print(f"I was born in the year 2002, and I am {age} years old now.")

# Improved Code with Variables
name = input("Hello, what is your name?\nName: ")
print(f"Hello, {name}!")

myDigits = 264890702902689430234689893469082346
myDigitsLength = len(str(myDigits))
print(f"The Digit \"{myDigits}\" has a total of {myDigitsLength} numbers")
print(f'The Digit "{myDigits}" has a total of {myDigitsLength} numbers')