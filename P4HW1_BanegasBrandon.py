# Brandon Banegas
# Date: 04/11/2026
# Assignment: P4HW1
# Description: Program collects scores, validates input, drops lowest score,
# calculates average, and assigns a letter grade.

# ----------- PSEUDOCODE -----------
# Ask user how many scores they want to enter
# Create an empty list to store scores
# Loop for the number of scores:
#     Ask user to enter a score
#     While score is invalid (<0 or >100):
#         Display error message
#         Ask for score again
#     Add valid score to list
# Find the lowest score
# Remove the lowest score from the list
# Calculate the average of remaining scores
# Determine letter grade based on average
# Display results

# Ask user for number of scores
num_scores = int(input("How many scores do you want to enter? "))

scores = []

# Loop to collect scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    # Validation loop
    while score < 0 or score > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i} again: "))

    scores.append(score)

# Find and remove lowest score
lowest = min(scores)
scores.remove(lowest)

# Calculate average
average = sum(scores) / len(scores)

# Determine letter grade
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Display results
print("\n------------Results------------")
print(f"Lowest Score  : {lowest}")
print(f"Modified List : {scores}")
print(f"Scores Average: {average:.2f}")
print(f"Grade         : {grade}")
print("--------------------------------")