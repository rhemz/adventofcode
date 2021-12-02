x, y, aim = 0, 0, 0

with open('input', 'r') as data:
    for cur in data:
        command = cur.strip().split(' ')
        mod = int(command[1])

        match command[0]:
            case 'up':
                aim -= mod
            case 'down':
                aim += mod
            case 'forward':
                x += mod
                y += aim * mod
        
print(f'{x}, {y}')
print(x * y)