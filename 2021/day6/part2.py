import collections

# part1 implementation is way too slow for this...

with open('input', 'r') as data:
    inputdata = [int(x) for x in data.readline().strip().split(',')]

days = 256
timer_counts = collections.defaultdict(int)

# seed counters
for i in inputdata:
    timer_counts[i] += 1

# no nested loops this time, just tick up counters
for day in range(1, days+1):
    new_fish = timer_counts[0]

    for i in range(8):
        timer_counts[i] = timer_counts[i+1]

    timer_counts[6] += new_fish  # cycle 0-timer fish
    timer_counts[8] = new_fish  # add new fish to the population

# this is comically faster...
print(sum(timer_counts.values()))