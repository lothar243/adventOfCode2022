from pprint import pprint
import sys

sample_input = """30373
25512
65332
33549
35390"""

def create_visible_bitmap(lines):
    visibleBitmap = [[True] * len(lines[0]) for _ in range(len(lines))]
    for y in range(1, len(lines) - 1):
        for x in range(1, len(lines[0]) - 1):
            visibleBitmap[y][x] = is_visible(lines, x, y)
    return visibleBitmap

def is_visible(lines: list, x: int, y: int):
    treeHeight = int(lines[y][x])
    visibleFromTop = True
    for otherY in range(0, y):
        if int(lines[otherY][x]) >= treeHeight:
            visibleFromTop = False
            break
    visibleFromBottom = True
    for otherY in range(y + 1, len(lines)):
        if int(lines[otherY][x]) >= treeHeight:
            visibleFromBottom = False
            break
    visibleFromLeft = True
    for otherX in range(0, x):
        if int(lines[y][otherX]) >= treeHeight:
            visibleFromLeft = False
            break
    visibleFromRight = True
    for otherX in range(x + 1, len(lines[0])):
        if int(lines[y][otherX]) >= treeHeight:
            visibleFromRight = False
            break
    return visibleFromTop or visibleFromBottom or visibleFromLeft or visibleFromRight

def count_visible_trees(visibleBitmap):
    visibleTrees = 0
    for row in visibleBitmap:
        visibleTrees += row.count(True)
    return visibleTrees

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]
    visibleTrees = create_visible_bitmap(lines)
    print(count_visible_trees(visibleTrees))