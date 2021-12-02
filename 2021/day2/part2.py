x, y, aim = 0, 0, 0

with open('input', 'r') as data:
    for cur in data:
        command = cur.strip().split(' ')
        mod = int(command[1])

        if command[0] == 'up':
            aim -= mod
        elif command[0] == 'down':
            aim += mod
        elif command[0] == 'forward':
            x += mod
            y += aim * mod

print(f'{x}, {y}')
print(x * y)