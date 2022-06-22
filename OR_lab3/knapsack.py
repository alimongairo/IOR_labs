import random
from collections import Counter


class Chromosome:
    def __init__(self, gens, weight, cost):
        self.gens = gens
        self.total_weight = weight
        self.total_cost = cost


def get_chromosome_rand(length, w, c):
    gens = [random.randint(0, 1) for _ in range(length)]
    weight, cost = calculation(gens,w,c)
    return Chromosome(gens=gens, weight=weight, cost=cost)


def get_chromosome_from_parents(parent1, parent2, cross_idx, w, c):
    gens = []
    for i in range(len(parent1.gens)):
        if i <= cross_idx:
            gens.append(parent1.gens[i])
        else:
            gens.append(parent2.gens[i])
    weight, cost = calculation(gens, w, c)
    return Chromosome(gens=gens, weight=weight, cost=cost)


def calculation(gens, weights, costs):
    result_weight = 0
    result_cost = 0
    for i in range(len(gens)):
        if gens[i] == 1:
            result_weight += weights[i]
            result_cost += costs[i]
    return result_weight, result_cost


def weight_check(chrom, max_w, costs, weights, bag_len):
    def reset_gen():
        values = []
        for i in range(bag_len):
            if chrom.gens[i] == 1:
                values.append([costs[i] / weights[i], i])
        values.sort()
        chrom.gens[values[0][1]] = 0
        chrom.total_weight -= weights[values[0][1]]
        chrom.total_cost -= costs[values[0][1]]

    chrom.total_weight = calculation(gens=chrom.gens,weights=weights,costs=costs)[0]
    while chrom.total_weight > max_w:
        reset_gen()
        chrom.total_weight = calculation(gens=chrom.gens,weights=weights,costs=costs)[0]


def mutation(chrom):
    chance = 0.001
    for i in range(len(chrom.gens)):
        if random.randint(0, 1000) / 1000 < chance:
            if chrom.gens[i] == 1:
                chrom.gens[i] = 0
            else:
                chrom.gens[i] = 1


def crossover(chromosomes, chances, bag_len, weights, costs):
    new_generation = []
    amount = len(chromosomes)
    new_generation.append(chromosomes[0])
    new_generation.append(chromosomes[1])
    for _ in range((amount // 2) - 1):
        parent1, parent2 = random.choices(population=chromosomes[2:], weights=chances[2:], k=2)
        cross_idx = random.randint(0, bag_len)
        chrom1 = get_chromosome_from_parents(parent1=parent1,parent2=parent2,cross_idx=cross_idx,w=weights,c=costs)
        chrom2 = get_chromosome_from_parents(parent1=parent2,parent2=parent1,cross_idx=cross_idx,w=weights,c=costs)
        w1, c1 = calculation(gens=chrom1.gens,weights=weights,costs=costs)
        w2, c2 = calculation(gens=chrom1.gens, weights=weights, costs=costs)
        new_generation.append(Chromosome(gens=chrom1.gens,weight=w1,cost=c1))
        new_generation.append(Chromosome(gens=chrom2.gens,weight=w2,cost=c2))
    if amount % 2 == 1:
        new_generation.append(chromosomes[-1])
    return new_generation


def selection_chances(chromosomes):
    chances = []
    group1, group2, group3, group4 = [], [], [], []
    for i in range(len(chromosomes)):
        if i <= len(chromosomes) / 4:
            group1.append(chromosomes[i])
        elif i <= len(chromosomes) / 2:
            group2.append(chromosomes[i])
        elif i <= 3 * len(chromosomes) / 4:
            group3.append(chromosomes[i])
        else:
            group4.append(chromosomes[i])
    for _ in group1:
        chances.append(0.5 / len(group1))
    for _ in group2:
        chances.append(0.3 / len(group2))
    for _ in group3:
        chances.append(0.15 / len(group3))
    for _ in group4:
        chances.append(0.05 / len(group4))
    return chances


def exit_condition(chromosomes, total):
    tmp = []
    for itm in chromosomes:
        tmp.append(str(itm.gens))
    count = Counter(tmp)
    for c in count.values():
        if c / total >= 0.6:
            return True
    return False


def genetic_algorythm(w, weights, costs, num_of_items):
    count_of_chromosomes = 250
    generation = [get_chromosome_rand(length=num_of_items,w=weights,c=costs) for _ in range(count_of_chromosomes)]
    for chromosome in generation:
        weight_check(chrom=chromosome,max_w=w,weights=weights,costs=costs,bag_len=num_of_items)
    generation.sort(key=lambda x: x.total_cost, reverse=True)

    for _ in range(100):
        chances = selection_chances(chromosomes=generation)
        generation = crossover(chromosomes=generation,chances=chances,bag_len=num_of_items,weights=weights,costs=costs)
        for chromosome in generation:
            mutation(chromosome)
        for chromosome in generation:
            weight_check(chrom=chromosome,max_w=w,weights=weights,costs=costs,bag_len=num_of_items)

        for chromosome in generation:
            chromosome.total_weight,chromosome.total_cost = calculation(chromosome.gens,weights,costs)
        generation.sort(key=lambda x: x.total_cost, reverse=True)

        if exit_condition(generation, count_of_chromosomes):
            break

    return generation[0].gens, generation[0].total_cost, generation[0].total_weight
