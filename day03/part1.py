import sys
import multiset
sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def find_duplicate(firstCompartment: str, secondCompartment: str):
    return set(firstCompartment).intersection(set(secondCompartment)).pop()
    print("Error, no duplicate found in line", lineString)

def get_priority(char: str):
    ordNum = ord(char)
    if ordNum <= 90:
        return ordNum - 38
    else:
        return ordNum - 96

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip() for line in inputfile.readlines()]

    sumOfPriorities = 0
    for line in lines:
        numPerCompartment = int(len(line) / 2)
        duplicateItem = find_duplicate(line[:numPerCompartment], line[numPerCompartment:])
        priority = get_priority(duplicateItem)
        sumOfPriorities += priority
        print(line, duplicateItem, priority)

    print(sumOfPriorities)