import sys
sample_input1 = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

sample_input = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

class Rope:
    def __init__(this, numRemainingKnots: int):
        this.head = {'x': 0, 'y': 0}
        this.tail = {'x': 0, 'y': 0}
        if numRemainingKnots > 0:
            this.nextRope = Rope(numRemainingKnots - 1)
        else:
            this.nextRope = None
    
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
        if abs(newX - this.tail['x']) > 1 or abs(newY - this.tail['y']) > 1:
            # the tail needs to move
            if newX == this.tail['x']:
                # just move the y
                this.tail['y'] += newY - this.head['y']
            elif newY == this.tail['y']:
                # just move the x
                this.tail['x'] += newX - this.head['x']
            else:
                # need to move diagonally
                if newX > this.tail['x']:
                    this.tail['x'] += 1
                elif newX < this.tail['x']:
                    this.tail['x'] -= 1
                if newY > this.tail['y']:
                    this.tail['y'] += 1
                elif newY < this.tail['y']:
                    this.tail['y'] -= 1
            this.head['x'] = newX
            this.head['y'] = newY
            if this.nextRope is not None:
                this.nextRope.move_head(this.tail['x'], this.tail['y'])
        else:
            # the tail doesn't need to move
            this.head['x'] = newX
            this.head['y'] = newY

    def tail_as_tuple(this):
        if this.nextRope is not None:
            return this.nextRope.tail_as_tuple()
        return this.tail['x'], this.tail['y']
    
    def get_extremes(self):
        if self.nextRope is not None:
            extremes = self.nextRope.get_extremes()
            extremes['minX'] = min(extremes['minX'], self.head['x'], self.tail['x'])
            extremes['maxX'] = max(extremes['maxX'], self.head['x'], self.tail['x'])
            extremes['minY'] = min(extremes['minY'], self.head['y'], self.tail['y'])
            extremes['maxY'] = max(extremes['maxY'], self.head['y'], self.tail['y'])
            return extremes
        else:
            return {'minX': min(self.head['x'], self.tail['x'], 0),
                    'maxX': max(self.head['x'], self.tail['x'], 0),
                    'minY': min(self.head['y'], self.tail['y'], 0),
                    'maxY': max(self.head['y'], self.tail['y'], 0),
                    }

    def mark_location(self, extremes: dict, charMap: list, label: int):
        if label == 0:
            markChar = 'H'
        else:
            markChar = str(label)
        if self.nextRope is not None:
            self.nextRope.mark_location(extremes, charMap, label + 1)
        else:
            charMap[self.tail['y'] - extremes['minY']][self.tail['x'] - extremes['minX']] = 'T'
        charMap[self.head['y'] - extremes['minY']][self.head['x'] - extremes['minX']] = markChar
    
def visualizeRope(rope: Rope):
    extremes = rope.get_extremes()
    width = extremes['maxX'] - extremes['minX'] + 1
    height = extremes['maxY'] - extremes['minY'] + 1
    charMap = [['.'] * width for _ in range(height)]
    charMap[-extremes['minY']][-extremes['minX']] = 's'
    rope.mark_location(extremes, charMap, 0)
    for row in charMap:
        print("".join(row))
    
    
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
    
    rope = Rope(8)
    visualizeRope(rope)
    print()
    visitedLocations = {(0, 0): True}

    for line in lines:
        direction, distance = line.split(' ')
        for _ in range(int(distance)):
            rope.move_direction(direction)
            visitedLocations[rope.tail_as_tuple()] = True
            visualizeRope(rope)
            print()
    
    print(len(visitedLocations.keys()))
