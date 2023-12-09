import sys
sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    numFullyContained = 0
    for line in lines:
        firstString, secondString = line.split(",")
        firstStart, firstStop = firstString.split("-")
        firstSet = set(range(int(firstStart), int(firstStop) + 1))
        secondStart, secondStop = secondString.split("-")
        secondSet = set(range(int(secondStart), int(secondStop) + 1))
        if firstSet.issubset(secondSet) or secondSet.issubset(firstSet):
            numFullyContained += 1
    print(numFullyContained)
