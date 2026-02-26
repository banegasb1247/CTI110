# Brandon Banegas
# 02/26/2026
# P1HW2 - Travel Expenses
# This program calculates travel expenses and shows the remaining balance.

"""
Pseudocode:
1. Display program title
2. Ask user for budget
3. Ask user for travel destination
4. Ask user for gas expense
5. Ask user for accommodation expense
6. Ask user for food expense
7. Add all expenses
8. Subtract total expenses from budget
9. Display travel expense summary and remaining balance
"""

print("This program calculates and displays travel expenses")

# Get user inputs
budget = float(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas = float(input("\nHow much do you think you will spend on gas? "))
hotel = float(input("\nApproximately, how much will you need for accommodation/hotel? "))
food = float(input("\nLast, how much do you need for food? "))

# Calculate expenses
total_expenses = gas + hotel + food
remaining_balance = budget - total_expenses

# Display results
print("\n------------Travel Expenses------------")
print("Location:", destination)
print("Initial Budget:", budget)
print("\nFuel:", gas)
print("Accommodation:", hotel)
print("Food:", food)
print("\nRemaining Balance:", remaining_balance)