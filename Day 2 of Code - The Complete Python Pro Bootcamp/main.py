# Subscripting
print("Hello, World!"[-4])

# String
print("123" + "456")

# Integer = Whole Number
print(123 + 456)

# Large Integers
print(123_456_789 + 123_456_789)

# Float = Floating Point Number
print(3.14159)

# Boolean
print(True)
print(False)

# Return as int type
len("Hello, World!")

# type function: To know what type of data holds
print(type("Hello, World!"))

# String Formatting
print(int("1") + int("1"))

print("Number of letters of your name: " + str(len(input("Enter your name: "))))

# Improved Code with f-String Format
name = input("Name: ")
lengthName = len(name)
print(f"Name Length: {lengthName}")

# PEMDAS
# Parentheses, Exponents, Multiplication, Division, Addition, Subtraction
print(1 + 2 - 3 * 4 ** (5 / 6))

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)


# BMI Calculator
print("BMI Calculator")

bodyWeight = float(input("Body Weight in KiloGram: "))
bodyHeight = float(input("Body Height in Centimeters: "))

bodyHeightIndex = bodyHeight / 100
finalBodyHeightIndex = bodyHeightIndex ** 2

finalBodyMassIndex = round(bodyWeight / finalBodyHeightIndex, 2)

print(f"Body Mass Index: {finalBodyMassIndex}")


# Number Manipulation
score = 0
score += 1
print(score)


# f-string
print(f"Your score is {score}")