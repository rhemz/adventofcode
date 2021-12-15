# its the lanernfish all over again

from collections import namedtuple, defaultdict
insertion = namedtuple('insertion', 'pair val')

with open('input', 'r') as data:
    data = data.readlines()

start = data[0].strip()
print(start)

insertions = [insertion(*l.split(' -> ')) for l in [t.strip() for t in data[2:]]]
ins_counts = {ins.pair: 0 for ins in insertions}
char_counts = defaultdict(int)

# seed pair counts from start string
for i in range(len(start) - 1):
    ins_counts[start[i:i + 2]] += 1

# loop through steps
num_steps = 40
for step in range(1, num_steps+1):
    print('Step {}'.format(step))
    step_counts = defaultdict(int)

    for pair, count in ins_counts.items():
        # should prob just make insertions a dict.  meh
        ins = next((ins for ins in insertions if ins.pair == pair), None)

        # tick up main character count
        char_counts[ins.val] += count

        # tick up permutations going into next step
        step_counts[pair[0] + ins.val] += count
        step_counts[ins.val + pair[1]] += count

    ins_counts = step_counts

chars_sorted = sorted(char_counts.items(), key=lambda kv: kv[1])
print(chars_sorted[-1][1] - chars_sorted[0][1] + 1)
