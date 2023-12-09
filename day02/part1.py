import sys

sample_input = """A Y
B X
C Z"""

# Loss = 0
# Tie = 3
# Win = 6
# Rock = A = X = 1
# Paper = B = Y = 2
# Scissors = C = Z = 3

round_score = {("A", "X"): 4, #Tie (3), 1 for rock
               ("A", "Y"): 8, #Win (6) 2 for paper
               ("A", "Z"): 3, #Loss, 3 for scissors
               ("B", "X"): 1, #Loss, 1 for rock
               ("B", "Y"): 5, #Tie, 2 for paper
               ("B", "Z"): 9, #Win, 3 for scissors
               ("C", "X"): 7, #Win, 1 for rock
               ("C", "Y"): 2, #loss, 2 for paper
               ("C", "Z"): 6  #tie, 3 for scissors
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