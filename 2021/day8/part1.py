with open('input', 'r') as data:
    inputdata = [val.strip().split(' | ') for val in data.readlines()]

print(sum([1 if len(v) in [2, 3, 4, 7] else 0 for v in sum([output.split(' ') for signals, output in inputdata], [])]))
