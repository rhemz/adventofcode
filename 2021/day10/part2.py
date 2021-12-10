with open('input', 'r') as data:
    inputdata = [val.strip() for val in data.readlines()]

openers = ('(', '[', '{', '<')
closers = (')', ']', '}', '>')
pairings = dict(zip(openers, closers))
syntax_points = dict(zip(closers, tuple(range(1, 5))))

scores = []
for line in inputdata:
    chunks = []
    corrupted = False
    for c in line:
        if c in openers:
            chunks.append(c)
        elif c in closers:
            last_opener = chunks.pop()
            if pairings[last_opener] == c:
                continue
            else:
                corrupted = True
                break

    if corrupted:
        continue

    print('{} is incomplete'.format(line))
    points = 0
    for c in reversed([pairings[o] for o in chunks]):
        points = points * 5 + syntax_points[c]

    scores.append(points)

scores.sort()
print(scores[len(scores)//2])
