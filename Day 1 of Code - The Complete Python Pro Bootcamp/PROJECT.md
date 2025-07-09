###### Day 1 of Code - The Complete Python Pro Bootcamp
### Band Name Generator
#### Objective
Create a simple Python program that generates a band name based on user input.

**What You Will Use:**
- print() for displaying messages to the user
- input() to receive user input from the keyboard
- String concatenation or f-strings to format and display the final output

#### Task:
Write a Python script that asks the user for:
1. What's the name of the city you grew up in?
2. What's your pet's name?

Then, combine both answers to suggest a potential band name.

**Expected Output Example:**
```text
Band Name: Manila Max
```

### Project Solution
```python
print('Welcome to the Band Name Generator')

cityName = input("What's the name of the city you grew up in?\nAnswer: ")
petName = input("What's your pet's name?\nAnswer: ")

print(f"Band Name: {cityName} {petName}")
```