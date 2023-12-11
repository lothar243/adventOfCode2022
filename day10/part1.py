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
    signalStrengthNum = 0
    while len(lines) > 0:
        line = lines.pop()
        if cycleNum in (20, 60, 100, 140, 180, 220):
            print(cycleNum, xReg)
            signalStrengthNum += cycleNum * xReg
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
    print(f"{xReg=}, {signalStrengthNum=}")
