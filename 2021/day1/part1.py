num_incr = -1
prev = -1

with open('input', 'r') as data:
    for cur in data:
        cur = int(cur)
        if cur > prev:
            num_incr += 1

        prev = cur

print(num_incr)
