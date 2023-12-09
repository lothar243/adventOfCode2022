import sys
sample_input = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""
# sys.argv = ['part1.py', '/home/jeff/Documents/adventOfCode2022/day05/input']

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    lineNumber = 0
    numStacks = int((len(lines[0]) + 1) / 4)
    stacks = [[] for _ in range(numStacks)]
    while not lines[lineNumber][1].isnumeric():
        for stackIndex in range(numStacks):
            char = lines[lineNumber][stackIndex * 4 + 1]
            if char != " ":
                stacks[stackIndex].append(char)
        lineNumber += 1
    for i in range(len(stacks)):
        stacks[i].reverse()
    print(stacks)

    lineNumber += 2
    
    for line in lines[lineNumber:]:
        numToMove, remainingLine = line[5:].split(" from ")
        numToMove = int(numToMove)
        fromStack, toStack = remainingLine.split(' to ')
        fromStack = int(fromStack) - 1
        toStack = int(toStack) - 1
        pickedUpCrates = []
        for _ in range(numToMove):
            pickedUpCrates.append(stacks[fromStack].pop())
        for _ in range(numToMove):
            stacks[toStack].append(pickedUpCrates.pop())
        print(f"{numToMove=}, {fromStack=}, {toStack=}")
    print(stacks)
    print("".join([stack.pop() for stack in stacks]))