import random
from typing import *


class Bag:
    def __init__(self, w: int, length: int, weights: list, costs: list):
        self.w = w
        self.weights = weights
        self.costs = costs
        self.len = length


class Chromosome:
    def __init__(self, parents: bool, bag: Bag, parent1=None, parent2=None, double=False):
        self.bag = bag

        if parents is True:
            try:
                if double == 0:
                    self.gens = []
                    for i in range(self.bag.len):
                        if parent1.gens[i] == parent2.gens[i]:
                            self.gens.append(parent1.gens[i])
                        else:
                            elem = parent1.gens[i] if random.randint(0, 1) == 0 else parent2.gens[i]
                            self.gens.append(elem)
                    self.mutation()
                else:
                    a = 1
                    # TODO how to create two chromosomes with different gens [0, 1, 0, 1], [0, 0, 1, 0] -> [0, 1, 1],
                    #  [0, 0, 0]
            except AttributeError:
                raise AttributeError('parents are not defined')
        else:
            self.gens = [random.randint(0, 1) for _ in range(self.bag.len)]

        self.cost = self.calculate_costs()

    def calculate_weight(self):
        result = 0
        for i in range(len(self.gens)):
            if self.gens[i] == 1:
                result += self.bag.weights[i]
        return result

    def calculate_costs(self):
        result = 0
        for i in range(len(self.gens)):
            if self.gens[i] == 1:
                result += self.bag.costs[i]
        return result

    def check(self):
        weight = self.calculate_weight()
        while weight > self.bag.w:
            self.reset_gen()
            weight = self.calculate_weight()

    def reset_gen(self):
        l = []
        for i in range(self.bag.len):
            if self.gens[i] == 1:
                l.append(i)
        rand = random.randint(0, len(l) - 1)
        self.gens[l[rand]] = 0

    def mutation(self):
        chance = 0.15
        for i in range(self.bag.len):
            if random.randint(0, 100) / 100 < chance:
                if self.gens[i] == 1:
                    self.gens[i] = 0
                else:
                    self.gens[i] = 1


def genne_algo(w, weights, costs):
    def calc_costs(chromosomes):
        chromo_costs = []
        for i, chromosome in enumerate(chromosomes):
            chromo_costs.append((chromosome.calculate_costs(), i))
        return chromo_costs

    bag = Bag(w=w, length=len(weights), weights=weights, costs=costs)
    count_of_chromosomes = 30
    chromosomes = [Chromosome(parents=False, bag=bag) for _ in range(count_of_chromosomes)]
    for chromosome in chromosomes:
        chromosome.check()

    chromosomes.sort(key=lambda x: x.cost)

    crossover(chormosomes=chromosomes, count=count_of_chromosomes, bag=bag)
    # TODO sort, but it need to keep index???
    # TODO reset gens if their weight > w
    # TODO sort by costs
    # TODO while 1: next generation (chances)


def crossover(chormosomes, count, bag):
    new_chromosomes = []
    chanses = [0.5 / 2 ** i for i in range(count - 1)]
    chanses.append(chanses[-1])
    parent1, parent2 = random.choices(chormosomes, weights=chanses, k=2)
    new_chromosomes.append(Chromosome(parents=True, bag=bag, parent1=parent1, parent2=parent2, double=True))
    # new_chromosomes.append(Chromosome(parents=True, bag=bag, parent1=parent1, parent2=parent2, double=True))


def chek_4_exit(chromosomes):
    if chromosomes[0] == chromosomes[1]:
        return True
    return False
    # TODO if 90% chromosome.gen equal, break


#
# class Population:
#     def __init__(self, chromosomes, bag):
#         self.bag = bag
#         self.chromosomes = chromosomes
#         self.amount = chromosomes.len
#         if chromosomes:
#             self.cromo_len = chromosomes[0].len
#
#
