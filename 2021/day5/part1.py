from collections import namedtuple


def get_points(p1, p2):
    if p1.x == p2.x:
        # vertical line
        y_range = sorted([p1.y, p2.y])
        return [point(p1.x, y) for y in range(y_range[0], y_range[1] + 1)]
    else:
        # horizontal line
        x_range = sorted([p1.x, p2.x])
        return [point(x, p1.y) for x in range(x_range[0], x_range[1]+1)]


lines = []
point = namedtuple('point', 'x y')
gridsize = 1000
grid = [[0] * gridsize for _ in range(gridsize)]

with open('input', 'r') as data:
    inputdata = [val.strip().split(' -> ') for val in data.readlines()]

for coordset in inputdata:
    lines.append((
        point(*[int(x) for x in coordset[0].split(',')]),
        point(*[int(x) for x in coordset[1].split(',')])
    ))

for p1, p2 in lines:
    if p1.x != p2.x and p1.y != p2.y:
        print('diagonal, skipping...')
        continue

    for p in get_points(p1, p2):
        grid[p.y][p.x] += 1

num_intersects = 0
for i in range(gridsize):
    for j in range(gridsize):
        if grid[i][j] > 1:
            print('got an intersect! {} points at {},{}'.format(grid[i][j], i, j))
            num_intersects += 1

print(num_intersects)
