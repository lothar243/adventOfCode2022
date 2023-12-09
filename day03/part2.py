import sys
import multiset
sample_input = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

def find_duplicate(first: str, second: str, third: str):
    return set(first).intersection(set(second)).intersection(set(third)).pop()

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
    for i in range(0, len(lines), 3):
        duplicateItem = find_duplicate(lines[i], lines[i + 1], lines[i + 2])
        priority = get_priority(duplicateItem)
        sumOfPriorities += priority
        print(i, duplicateItem, priority)

    print(sumOfPriorities)