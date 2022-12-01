from pprint import pprint

allElves = []
with open("input.txt", 'r') as infile:
    currentElf = []
    for line in infile:
        if line.isspace():
            allElves.append(currentElf)
            currentElf = []
        else:
            currentElf.append(int(line.strip()))

elfTotals = sorted([sum(elfLoad) for elfLoad in allElves])
print(elfTotals[-1] + elfTotals[-2] + elfTotals[-3])