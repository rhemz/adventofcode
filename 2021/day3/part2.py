
def filter_bits(inp, width, most=True):
    for i in range(bit_width):
        zeros = [x[i] for x in inp].count('0')
        ones = len(inp) - zeros

        if most:
            sb = '1' if ones >= zeros else '0'
        else:
            sb = '0' if zeros <= ones else '1'

        filtered_bits = [x for x in inp if x[i] == sb]
        if len(filtered_bits) == 1:
            return filtered_bits[0]

        inp = filtered_bits


with open('input', 'r') as data:
    all_values = [val.strip() for val in data.readlines()]

bit_width = len(all_values[0])
oxygen = int(filter_bits(all_values, bit_width), 2)
co2 = int(filter_bits(all_values, bit_width, False), 2)
