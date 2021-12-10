with open('input', 'r') as data:
    inputdata = [val.strip() for val in data.readlines()]

openers = ('(', '[', '{', '<')
closers = (')', ']', '}', '>')
pairings = dict(zip(openers, closers))
syntax_points = dict(zip(closers, (3, 57, 1197, 25137)))

points = 0
for line in inputdata:
    chunks = []
    corrupted = False
    for c in line:
        if c in openers:
            chunks.append(c)
        elif c in closers:
            if pairings[chunks.pop()] == c:
                continue
            else:
                corrupted = True
                points += syntax_points[c]
                break

    if corrupted:
        print('{} is corrupted'.format(line))
        continue

print(points)
