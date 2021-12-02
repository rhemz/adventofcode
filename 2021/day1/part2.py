num_incr = -1
cur = 0
prev = -1

with open('input', 'r') as data:
    all_values = [int(val) for val in data.readlines()]

for i in range(len(all_values) - 2):
    cur = sum(all_values[i:i+3])
    if cur > prev:
        num_incr += 1

    prev = cur

print(num_incr)
