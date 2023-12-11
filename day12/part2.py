import sys
from heapq import heappush, heappop

sample_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""

def find_symbol(maze: list, symbol):
    for y, line in enumerate(maze):
        x = line.find(symbol)
        if x != -1:
            return x, y

def get_adjacent(location, width, height, lines):
    x = location[0]
    y = location[1]
    currentLevel = ord(lines[y][x])
    adjacent = []
    if x > 0 and currentLevel - 1 <= ord(lines[y][x - 1]):
        adjacent.append((x - 1, y))
    if x < width - 1 and currentLevel - 1 <= ord(lines[y][x + 1]):
        adjacent.append((x + 1, y))
    if y > 0 and currentLevel - 1 <= ord(lines[y - 1][x]):
        adjacent.append((x, y - 1))
    if y < height - 1 and currentLevel - 1 <= ord(lines[y + 1][x]):
        adjacent.append((x, y + 1))
    return adjacent
        
def manhattan_distance(position1: tuple, position2: tuple):
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]

    height = len(lines)
    width = len(lines[0])
    startLocation = find_symbol(lines, 'S')
    endLocation = find_symbol(lines, 'E')
    lines[startLocation[1]] = lines[startLocation[1]].replace('S', 'a')
    lines[endLocation[1]] = lines[endLocation[1]].replace('E', 'z')

    distances = [[1e10] * width for _ in range(height)]
    nodesToVisit = [(0, endLocation, 0)]
    endFound = False
    while not endFound:
        node = heappop(nodesToVisit)
        priority, location, distance = node
        #print(node)
        if lines[location[1]][location[0]] == 'a':
            print(f"{distance=}")
            exit()
        if distance < distances[location[1]][location[0]]:
            distances[location[1]][location[0]] = distance
            pass
            for adjacent in get_adjacent(location, width, height, lines):
                heappush(nodesToVisit, (distance + 1,
                                        adjacent,
                                        distance + 1))