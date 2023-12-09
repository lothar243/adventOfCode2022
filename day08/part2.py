from pprint import pprint
import sys

sample_input = """30373
25512
65332
33549
35390"""

def compute_scenic_score(lines: list, x: int, y: int):
    treeHeight = int(lines[y][x])
    # looking up
    numTreesAbove = 0
    for otherY in range(y - 1, -1, -1):
        numTreesAbove += 1
        if treeHeight <= int(lines[otherY][x]):
            break
    # looking down
    numTreesBelow = 0
    for otherY in range(y + 1, len(lines)):
        numTreesBelow += 1
        if treeHeight <= int(lines[otherY][x]):
            break
    # looking left
    numTreesLeft = 0
    for otherX in range(x - 1, -1, -1):
        numTreesLeft += 1
        if treeHeight <= int(lines[y][otherX]):
            break
    # looking right
    numTreesRight = 0
    for otherX in range(x + 1, len(lines[0])):
        numTreesRight += 1
        if treeHeight <= int(lines[y][otherX]):
            break
    return numTreesAbove * numTreesBelow * numTreesLeft * numTreesRight

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    scenicScores = []
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            scenicScores.append(compute_scenic_score(lines, x, y))
    print(max(scenicScores))