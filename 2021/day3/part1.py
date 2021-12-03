
with open('input', 'r') as data:
    all_values = [val.strip() for val in data.readlines()]

bit_width = len(all_values[0])
most_common, least_common = [], []

for i in range(bit_width):
    bits = [x[i] for x in all_values]
    mcb = max(bits, key=bits.count)
    most_common.append(mcb)
    least_common.append(str(1 - int(mcb)))

gamma = int(''.join(most_common), 2)
epsilon = int(''.join(least_common), 2)

print(gamma * epsilon)