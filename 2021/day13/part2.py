from collections import namedtuple
point = namedtuple('point', 'x y')
fold = namedtuple('fold', 'axis val')


def fold_grid(grid, f):
    if f.axis == 'y':
        ngrid = grid[:f.val]
        ogrid = grid[f.val+1:]
    else:
        ngrid, ogrid = [], []
        for y in range(len(grid)):
            ngrid.append(grid[y][:f.val])
            ogrid.append(grid[y][f.val+1:])

    # reflect
    for y in range(len(ogrid)):
        for x in range(len(ogrid[0])):
            v = ogrid[y][x]
            if v > 0:
                if f.axis == 'y':
                    ngrid[len(ngrid) - y - 1][x] = 1
                else:
                    ngrid[y][len(ngrid[y]) - x - 1] = 1

    return ngrid


mx, my = 0, 0
points = []
folds = []

with open('input', 'r') as data:
    data = data.read()
    coords, instrs = data.split('\n\n')

for line in coords.split('\n'):
    line = line.strip().split(',')
    x = int(line[0])
    y = int(line[1])
    if x > mx:
        mx = x
    if y > my:
        my = y
    points.append(point(x, y))

for instr in instrs.strip().split('\n'):
    axis, val = instr[11:].split('=')
    folds.append(fold(axis, int(val)))

# make a big empty grid
grid = [[0] * (mx+1) for _ in range(my+1)]

for p in points:
    grid[p.y][p.x] = 1

for f in folds:
    grid = fold_grid(grid, f)

for row in grid:
    print(''.join(['█' if x == 1 else ' ' for x in row]))
