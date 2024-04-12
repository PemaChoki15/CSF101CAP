##########################################
# Name: Pema Choki
# Department: Electrical Department
# Student ID no: 02230068
##########################################
# References
# CSF Unit Guides and Notes
# https://github.com/topics/rock-paper-scissor-python
# https://youtu.be/LpZmZs2_BC4?si=SxvYGCRSV_TGRYV4
##########################################
# Solution
# Your Solution Score: 49960
# Put your number here:
##########################################

# Read the input file
input_file = "input_8_cap1.txt"  # Use your input file name
rounds = []

with open('C:/Users/Ugyen/Downloads/input_8_cap1.txt', 'r') as f:
    for line in f:
        opponent_chooses, desired_outcome = line.strip().split()
        rounds.append((opponent_chooses, desired_outcome))

# Calculate the score
total_score = 0

for opponent_chooses, desired_outcome in rounds:
    if desired_outcome == 'X':
        if opponent_chooses == 'A':
            total_score += 1 + 0  # Rock loses to Paper
        elif opponent_chooses == 'B':
            total_score += 2 + 0  # Paper loses to Scissors
        elif opponent_chooses == 'C':
            total_score += 3 + 0  # Scissors loses to Rock
    elif desired_outcome == 'Y':
        if opponent_chooses == 'A':
            total_score += 1 + 3  # To have draw, choose rock
        elif opponent_chooses == 'B':
            total_score += 2 + 3  # To have draw, choose paper
        elif opponent_chooses == 'C':
            total_score += 3 + 3  # To have draw, choose scissor
    elif desired_outcome == 'Z':
        if opponent_chooses == 'A':
            total_score += 1 + 6  # Rock wins against Scissors
        elif opponent_chooses == 'B':
            total_score += 2 + 6  # Paper wins against Rock
        elif opponent_chooses == 'C':
            total_score += 3 + 6  # Scissors wins against Paper

# Print the total score
print("Total score:", total_score)
