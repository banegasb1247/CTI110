# Brandon Banegas
# Date: 04/24/2026
# Assignment: P5LAB
# Description: Simulates a self-checkout system and calculates change

import random

# Function to calculate and display change
def disperse_change(change):
    # Convert to cents to avoid float issues
    cents = int(round(change * 100))

    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25

    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    if dollars > 0:
        print(f"{dollars} Dollars")
    if quarters > 0:
        print(f"{quarters} Quarters")
    if dimes > 0:
        print(f"{dimes} Dimes")
    if nickels > 0:
        print(f"{nickels} Nickels")
    if pennies > 0:
        print(f"{pennies} Pennies")


# Main function
def main():
    # Generate random total owed
    total_owed = round(random.uniform(0.01, 100.00), 2)

    print(f"You owe ${total_owed:.2f}")

    # Get user input
    cash = float(input("How much cash will you put in the self-checkout? "))

    # Calculate change
    change = round(cash - total_owed, 2)

    if change < 0:
        print("Not enough money provided.")
    else:
        print(f"Change is: ${change:.2f}")
        disperse_change(change)


# Call main
main()