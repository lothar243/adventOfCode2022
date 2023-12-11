import sys

sample_input = """noop
addx 3
addx -5"""

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    lines.reverse()
    cycleNum = 1
    xReg = 1
    while len(lines) > 0:
        if abs(cycleNum % 40 - 1 - xReg) <= 1:
            print("#", end="")
        else:
            print(".", end="")
        if cycleNum %40 == 0:
            print()
        line = lines.pop()
        if line == "noop":
            pass
        elif line.startswith("addx "):
            instruction, value = line.split(" ")
            lines.append("addx2 " + value)
        elif line.startswith("addx2"):
            instruction, value = line.split(" ")
            value = int(value)
            xReg += value
        cycleNum += 1
