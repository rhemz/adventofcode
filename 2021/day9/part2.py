import math

with open('input', 'r') as data:
    inputdata = [[int(c) for c in val.strip()] for val in data.readlines()]

width = len(inputdata[0])
height = len(inputdata)

def surrounding(x, y):
    neighbors = []
    # get value above.  for pt 2 return the position as well
    if y > 0:
        neighbors.append((inputdata[y-1][x], x, y-1))
    # get value below
    if y < height - 1:
        neighbors.append((inputdata[y+1][x], x, y+1))
    # get value to left
    if x > 0:
        neighbors.append((inputdata[y][x-1], x-1, y))
    # get value to right
    if x < width - 1:
        neighbors.append((inputdata[y][x+1], x+1, y))

    return neighbors

def explore_basin(x, y, size, seen_points):
    for val, nx, ny in surrounding(x, y):
        if val == 9:
            continue

        if (nx, ny) in seen_points:
            continue

        size += 1
        seen_points.append((nx, ny))
        size = explore_basin(nx, ny, size, seen_points)

    return size

# find low points
low_points = []
for y in range(len(inputdata)):
    for x in range(len(inputdata[y])):
        neighbors = surrounding(x, y)
        if all(inputdata[y][x] < n[0] for n in neighbors):
            low_points.append((x, y))

# find each basin starting from the low points
basin_sizes = []
for p in low_points:
    size = explore_basin(p[0], p[1], 0, [])
    basin_sizes.append(size)

print(math.prod(sorted(basin_sizes)[-3:]))
