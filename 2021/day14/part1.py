from collections import namedtuple
insertion = namedtuple('insertion', 'pair val')

with open('input', 'r') as data:
    data = data.readlines()

start = data[0].strip()
# insertions = [insertion(tuple(p[0]), p[1]) for p in [l.split(' -> ') for l in [t.strip() for t in data[2:]]]]
insertions = [insertion(*l.split(' -> ')) for l in [t.strip() for t in data[2:]]]
print(start)
num_steps = 10

current = start
for step in range(1, num_steps+1):
    ins_positions = []

    for i in range(len(current) - 1):
        pair = current[i:i+2]

        for ins in insertions:
            if pair == ins.pair:
                ins_positions.append((i, ins.val))

    new_poly = list(current)
    for p in reversed(ins_positions):
        new_poly.insert(p[0]+1, p[1])

    current = ''.join(new_poly)
    print('Step {}: {}'.format(step, current))

char_counts = {c: current.count(c) for c in set(current)}
chars_sorted = sorted(char_counts.items(), key=lambda kv: kv[1])

print(chars_sorted[-1][1] - chars_sorted[0][1])