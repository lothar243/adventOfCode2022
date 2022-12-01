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
print("The elf with the largest load has {} calories".format(elfTotals[-1]))
print("The sum of the top three elfs is {} calories".format(elfTotals[-1] + elfTotals[-2] + elfTotals[-3]))