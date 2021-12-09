with open('input', 'r') as data:
    inputdata = [[int(c) for c in val.strip()] for val in data.readlines()]

# this would be like 3 lines with scipy convolve

width = len(inputdata[0])
height = len(inputdata)


def surrounding(x, y):
    neighbors = []
    # get value above.  can't just loop try/except because of python list slicing
    if y > 0:
        neighbors.append(inputdata[y-1][x])
    # get value below
    if y < height - 1:
        neighbors.append(inputdata[y+1][x])
    # get value to left
    if x > 0:
        neighbors.append(inputdata[y][x-1])
    # get value to right
    if x < width - 1:
        neighbors.append(inputdata[y][x+1])

    return neighbors


low_points = []
for y in range(len(inputdata)):
    for x in range(len(inputdata[y])):
        neighbors = surrounding(x, y)
        if all(inputdata[y][x] < n for n in neighbors):
            low_points.append(inputdata[y][x])

print(sum([x+1 for x in low_points]))
