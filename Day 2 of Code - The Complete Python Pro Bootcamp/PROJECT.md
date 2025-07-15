###### Day 2 of Code - The Complete Python Pro Bootcamp  
### Tip Calculator  
#### Objective  
Create a Python script that calculates how much each person should pay after adding a tip to the total bill and splitting it evenly.

**What You Will Use:**  
- `print()` to display prompts and results  
- `input()` to get user input  
- `float` and `int` for number conversion  
- Basic math operations (`*`, `/`, `+`)  
- `round()` to limit the final value to 2 decimal places  

#### Task:  
Write a Python script that asks the user for:  
1. The total bill amount  
2. The tip percentage they'd like to give (e.g., 10, 12, or 15)  
3. The number of people splitting the bill  

Then calculate and show how much each person should pay.

**Expected Output Example:**
```text
Welcome to the tip calculator!
What was the total bill?
$150
How much tip would you like to give?
10%, 12%, or 15%
Tip Percent: 10
How many people to split the bill?
Split the into: 5
Each person should pay: $33.0
```

### Project Solution
```python
print("Welcome to the tip calculator!")

bill_amount = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? (10, 12, or 15): "))
num_people = int(input("How many people to split the bill? "))

tip_decimal = tip_percent / 100
total_with_tip = bill_amount + (bill_amount * tip_decimal)
amount_per_person = round(total_with_tip / num_people, 2)

print(f"Each person should pay: ${amount_per_person}")
```