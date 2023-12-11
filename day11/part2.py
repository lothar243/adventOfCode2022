import sys
from pprint import pprint

sample_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

def throw_items(monkeys, monkeyNum, modulus):
    monkey = monkeys[monkeyNum]
    while len(monkey['items']) > 0:
        old = monkey['items'].pop(0)
        new = eval(monkey['operation']) % modulus
        if new % monkey['test'] == 0:
            monkeys[monkey['ifTrue']]['items'].append(new)
        else:
            monkeys[monkey['ifFalse']]['items'].append(new)
        monkey['numInspections'] += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    monkeys = []
    lineNum = 0
    modulus = 1
    while lineNum < len(lines) - 1:
        name = lines[lineNum]
        items = [int(val) for val in lines[lineNum + 1].split(": ")[1].split(", ")]
        operation = lines[lineNum + 2].split(" ", 5)[-1]
        test = int(lines[lineNum + 3].split(" ")[-1])
        modulus *= test
        ifTrue = int(lines[lineNum + 4].split(" ")[-1])
        ifFalse = int(lines[lineNum + 5].split(" ")[-1])
        monkeys.append({
            "name": name,
            "items": items,
            "operation": operation,
            "test": test,
            "ifTrue": ifTrue,
            "ifFalse": ifFalse,
            "numInspections": 0
            })
        lineNum += 7
    
    for roundNum in range(10000):
        for monkeyNum in range(len(monkeys)):
            throw_items(monkeys, monkeyNum, modulus)
    
    inspectionList = [monkey['numInspections'] for monkey in monkeys]
    inspectionList.sort()

    print(inspectionList[-2] * inspectionList[-1])
