import random
from collections import Counter


class Chromosome:
    def __init__(self, gens, matrix):
        self.gens = gens
        self.matrix = matrix
        self.positions = self.create_dict()
        self.distance = self.calculate_distance()

    def create_dict(self):
        positions = {}
        for i, gen in enumerate(self.gens):
            positions[gen] = i
        return positions

    def calculate_distance(self):
        vertex_amount = len(self.gens)
        dist = 0
        for i in range(vertex_amount - 1):
            dist += self.matrix[self.gens[i]][self.gens[i + 1]]
        dist += self.matrix[self.gens[-1]][self.gens[0]]
        return dist


def get_chromosome_rand(length, matrix):
    gens = [i for i in range(length)]
    random.shuffle(gens)
    return Chromosome(gens=gens, matrix=matrix)


def ordered_crossover(parent1, parent2):
    length = len(parent1)
    idx1 = random.randint(0,length-2)
    idx2 = random.randint(idx1+1,length-1)
    mid1 = parent1[idx1:idx2]
    mid2 = parent2[idx1:idx2]

    tmp_p2 = parent2[idx2:length] + parent2[0:idx2]
    for i in mid1:
        tmp_p2.remove(i)

    tmp_p1 = parent1[idx2:length] + parent1[0:idx2]
    for i in mid2:
        tmp_p1.remove(i)

    child1 = tmp_p2[0:idx1] + mid1 + tmp_p2[idx1:]
    child2 = tmp_p1[0:idx1] + mid2 + tmp_p1[idx1:]
    return child1, child2


def swap_mutation(chromosome):
    chance = 0.01
    if random.randint(0, 100) / 100 < chance:
        idx1, idx2 = 0, 0
        while idx1 == idx2:
            idx1 = random.randint(0, len(chromosome.gens)-1)
            idx2 = random.randint(0, len(chromosome.gens)-1)
        chromosome.gens[idx1], chromosome.gens[idx2] = chromosome.gens[idx2], chromosome.gens[idx1]
    return chromosome


def crossover(chromosomes, chances, matrix):
    new_generation = []
    amount = len(chromosomes)
    new_generation.append(chromosomes[0])
    new_generation.append(chromosomes[1])
    for _ in range((amount // 2) - 1):
        parent1, parent2 = random.choices(population=chromosomes, weights=chances, k=2)
        chrom1_gens, chrom2_gens = ordered_crossover(parent1=parent1.gens,parent2=parent2.gens)
        new_generation.append(Chromosome(gens=chrom1_gens,matrix=matrix))
        new_generation.append(Chromosome(gens=chrom2_gens,matrix=matrix))
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


def genetic_algorythm(matrix):
    count_of_chromosomes = 250
    vertex_amount = len(matrix[0])
    generation = [get_chromosome_rand(length=vertex_amount,matrix=matrix) for _ in range(count_of_chromosomes)]
    generation.sort(key=lambda x: x.distance)

    for _ in range(100):
        chances = selection_chances(chromosomes=generation)
        generation = crossover(chromosomes=generation,chances=chances,matrix=matrix)
        for chromosome in generation:
            swap_mutation(chromosome)

        generation.sort(key=lambda x: x.distance)

        if exit_condition(generation, count_of_chromosomes):
            break

    return generation[0].gens, generation[0].distance
