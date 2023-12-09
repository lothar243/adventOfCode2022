import sys
sample_input = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

class Rope:
    def __init__(this, head: dict, tail: dict):
        this.head = head
        this.tail = tail
    
    def move_direction(this, direction):
        if direction == 'R':
            this.move_head(this.head['x'] + 1, this.head['y'])
        if direction == 'L':
            this.move_head(this.head['x'] - 1, this.head['y'])
        if direction == 'U':
            this.move_head(this.head['x'], this.head['y'] - 1)
        if direction == 'D':
            this.move_head(this.head['x'], this.head['y'] + 1)

    def move_head(this, newX, newY):
        if newX == this.head['x']:
            # moving y only
            if abs(newY - this.tail['y']) > 1:
                # move the tail to the old head's location
                this.tail['y'] = this.head['y']
                this.tail['x'] = this.head['x']
            this.head['y'] = newY
        if newY == this.head['y']:
            # moving x only
            if abs(newX - this.tail['x']) > 1:
                # move the tail to the old head's location
                this.tail['y'] = this.head['y']
                this.tail['x'] = this.head['x']
            this.head['x'] = newX
    
    def tail_as_tuple(this):
        return this.tail['x'], this.tail['y']
    
def visualize_visited(visited: dict):
    visitedXs = [location[0] for location in visited.keys()]
    minX = min(visitedXs)
    maxX = max(visitedXs)

    visitedYs = [location[1] for location in visited.keys()]
    minY = min(visitedYs)
    maxY = max(visitedYs)
    charMap = [ (['.'] * (maxX - minX + 1)) for _ in range(maxY - minY + 1)]
    for location in visited.keys():
        charMap[location[1] - minY][location[0] - minX] = '#'
    charMap[-minY][-minX] = 's'
    return charMap

if __name__ == "__main__":
    if len(sys.argv) < 2:
        lines = sample_input.split("\n")
    else:
        with open(sys.argv[1]) as inputfile:
            lines = [line.strip("\n") for line in inputfile.readlines()]
    
    visited = {(0,0): True}
    rope = Rope({'x': 0, 'y': 0}, {'x': 0, 'y': 0})
    for line in lines:
        direction, distance = line.split(' ')
        distance = int(distance)
        for _ in range(distance):
            rope.move_direction(direction)
            visited[rope.tail_as_tuple()] = True
    
    
    for line in visualize_visited(visited):
        print("".join(line))
    
    print(len(list(visited.keys())))
                
