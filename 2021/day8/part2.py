import itertools

with open('input', 'r') as data:
    inputdata = [val.strip().split(' | ') for val in data.readlines()]

'''
     aaaa  
    b    c 
    b    c 
     dddd  
    e    f 
    e    f 
     gggg  
'''
all_chars = 'abcdefg'
signal_map = {
    'abcefg':   '0',
    'cf':       '1',
    'acdeg':    '2',
    'acdfg':    '3',
    'bcdf':     '4',
    'abdfg':    '5',
    'abdefg':   '6',
    'acf':      '7',
    all_chars:  '8',
    'abcdfg':   '9'
}

def sort_against_map(map, val):
    return sorted(map[char] for char in val)

total = 0
for signals, output in inputdata:
    signals = [tuple(sig) for sig in signals.split()]
    output = [tuple(out) for out in output.split()]

    valid_map = None
    for perm in itertools.permutations(all_chars):
        perm_map = {k: v for k, v in zip(all_chars, perm)}

        if all([''.join(sort_against_map(perm_map, sig)) in signal_map.keys() for sig in signals]):
            valid_map = perm_map
            break

    # now that a valid mapping has been found, build the number from the output
    nums = []
    for num in output:
        decoded = signal_map[''.join(sort_against_map(valid_map, num))]
        nums.append(decoded)

    total += int(''.join(nums))

print(total)
