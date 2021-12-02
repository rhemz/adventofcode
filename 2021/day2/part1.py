x, y = 0, 0

with open('input', 'r') as data:
    for cur in data:
        command = cur.strip().split(' ')
        mod = int(command[1])
        if command[0] == 'forward':
            x += mod
        elif command[0] == 'up':
            y -= mod
        elif command[0] == 'down':
            y += mod

print(f'{x}, {y}')
print(x * y)