from collections import namedtuple
point = namedtuple('point', 'x y')

with open('input', 'r') as data:
    grid = [[int(v) for v in val.strip()] for val in data.readlines()]


def surrounding(grid, p):
    points = []
    # previous row
    if p.y > 0:
        points.extend([point(i, p.y-1) for i in range(max(p.x-1, 0), min(p.x+2, len(grid[p.y-1])))])
    # same row
    if p.x > 0:
        points.append(point(p.x-1, p.y))
    if p.x < len(grid[p.y])-1:
        points.append(point(p.x+1, p.y))
    # next row
    if p.y < len(grid) - 1:
        points.extend([point(i, p.y+1) for i in range(max(p.x-1, 0), min(p.x+2, len(grid[p.y+1])))])

    return points


def flash_sequence(grid, fgrid, p, t=9):
    fgrid[p.y][p.x] = True  # mark as flashed
    grid[p.y][p.x] = 0

    surr = surrounding(grid, p)
    for s in surr:
        if not fgrid[s.y][s.x]:  # if it hasn't already flashed
            grid[s.y][s.x] += 1

            if grid[s.y][s.x] > t:
                flash_sequence(grid, fgrid, s)


make_grid = lambda x: [[x] * len(grid) for _ in range(len(grid[0]))]

# visualize
print('starting grid')
[print(row) for row in grid]

total_flashes = 0
step = 1

while True:
    # fresh flashed status grid
    fgrid = make_grid(False)

    # increase energy level of everything by 1
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] += 1

    # loop through grid
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] > 9:
                print('starting flash_sequence call at {},{}'.format(x, y))
                flash_sequence(grid, fgrid, point(x, y))

    total_flashes += sum((1 if x else 0 for x in sum(fgrid, [])))

    # visualize
    print('after step {}'.format(step))
    [print(row) for row in grid]

    step += 1

    # is whole grid the same?
    if all(x == grid[0][0] for x in sum(grid, [])):
        break

print(total_flashes)