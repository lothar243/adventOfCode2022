import sys

sample_input = """A Y
B X
C Z"""

# Loss = 0 = X
# Tie = 3 = Y
# Win = 6 = Z
# Rock = A = 1
# Paper = B = 2
# Scissors = C = 3

round_score = {("A", "X"): 3, #Loss, 3 for scissors
               ("A", "Y"): 4, #Tie, 1 for rock
               ("A", "Z"): 8, #Win, 2 for paper
               # opponent choose paper
               ("B", "X"): 1, #Loss, 1 for rock
               ("B", "Y"): 5, #Tie, 2 for paper
               ("B", "Z"): 9, #Win, 3 for scissors
               # opponent chooses scissors
               ("C", "X"): 2, #Loss, 2 for paper
               ("C", "Y"): 6, #Tie, 3 for scissors
               ("C", "Z"): 7  #Win, 1 for rock
}

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    total_score = 0
    for line in lines:
        opponent, mine = line.split(" ")
        total_score += round_score[(opponent, mine)]
    
    print(total_score)