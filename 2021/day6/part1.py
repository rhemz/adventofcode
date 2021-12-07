class LanternFish:
    def __init__(self, timer):
        self.timer = timer

    def tick(self):
        if self.timer == 0:
            # reset to 6, make new fish
            self.timer = 6
            return LanternFish(timer=8)
        else:
            self.timer -= 1
            

with open('input', 'r') as data:
    inputdata = [int(x) for x in data.readline().strip().split(',')]

days = 80
population = []
# seed the population from input data
for i in inputdata:
    population.append(LanternFish(timer=i))

# simulate
for day in range(1, days+1):
    print('day {}, {} fish'.format(day, len(population)))
    todays_spawn = []
    for fish in population:
        newfish = fish.tick()
        if newfish is not None:
            todays_spawn.append(newfish)

    population = [*population, *todays_spawn]

print('Final Population: {}'.format(len(population)))