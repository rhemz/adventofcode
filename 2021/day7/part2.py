import sys

with open('input', 'r') as data:
    inputdata = [int(x) for x in data.readline().strip().split(',')]

least_fuel = sys.maxsize
best_position = None
for i in range(min(inputdata), max(inputdata)):
    fuel = 0
    for pos in inputdata:
        dist = abs(pos - i)
        fuel += int((dist * (dist + 1)) / 2)  # gauss sum

    if fuel < least_fuel:
        least_fuel = fuel
        best_position = i

print(best_position, least_fuel)
