import random
from collections import Counter


class Matrix:
    def __init__(self, matrix, count_of_vertex):
        self.matrix = matrix
        self.count_of_vertex = count_of_vertex


class Chromosome:
    def __init__(self, matrix, parents, parent1=None):
        self.matrix = matrix
        self.gens = [None for _ in range(self.matrix.count_of_vertex)]

        if parents:
            if isinstance(parent1,list):
                self.gens = parent1
            else:
                self.gens = parent1.gens

        else:
            self.gens = [i for i in range(self.matrix.count_of_vertex)]
            random.shuffle(self.gens)
        self.positions = self.create_dict()
        self.distance = self.calculate_distance()

    def create_dict(self):
        positions = {}
        for i, gen in enumerate(self.gens):
            positions[gen] = i
        return positions

    def calculate_distance(self):
        dist = 0
        for i in range(self.matrix.count_of_vertex - 1):
            dist += self.matrix.matrix[self.gens[i]][self.gens[i + 1]]
        dist += self.matrix.matrix[self.gens[-1]][self.gens[0]]
        return dist

    def mutation(self):
        chance = 0.001
        for i in range(self.matrix.count_of_vertex):
            if random.randint(0, 1000) / 1000 < chance:
                j = random.randint(0, self.matrix.count_of_vertex - 1)
                while j == i:
                    j = random.randint(0, self.matrix.count_of_vertex - 1)
                self.gens[i], self.gens[j] = self.gens[j], self.gens[i]


def ordered_crossover(list1, list2):
    l = len(list1)
    idx1 = random.randint(0,l-2)
    idx2 = random.randint(idx1+1,l-1)
    mid1 = list1[idx1:idx2]
    mid2 = list2[idx1:idx2]

    tmp_p2 = list2[idx2:l] + list2[0:idx2]
    for i in mid1:
        tmp_p2.remove(i)

    tmp_p1 = list1[idx2:l] + list1[0:idx2]
    for i in mid2:
        tmp_p1.remove(i)

    res1 = tmp_p2[0:idx1] + mid1 + tmp_p2[idx1:]
    res2 = tmp_p1[0:idx1] + mid2 + tmp_p1[idx1:]

    # set1, set2 = set(res1), set(res2)
    # if len(set1) != len(res1) or len(set2) != len(res2):
    #     print()

    return res1, res2


def swap(list_2_swap, i, j):
    if i == j:
        return list_2_swap
    elif i > j:
        i, j = j, i
    temp = list_2_swap[i: j + 1]
    temp.reverse()
    list_2_swap[i: j + 1] = temp
    return list_2_swap


def crossover(chromosomes, chances, matrix):
    new_generation = []
    amount = len(chromosomes)
    new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=chromosomes[0]))
    new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=chromosomes[1]))
    for _ in range((amount // 2) - 1):
        parent1, parent2 = random.choices(population=chromosomes[2:], weights=chances[2:], k=2)
        if random.randint(0, 100) < 85:
            child1, child2 = ordered_crossover(list1=parent1.gens, list2=parent2.gens)
            new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=child1))
            new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=child2))
        else:
            new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=parent1))
            new_generation.append(Chromosome(matrix=matrix, parents=True, parent1=parent2))
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


def check_4_exit(chromosomes, count_of_chromosomes):
    tmp = []
    for itm in chromosomes:
        tmp.append(str(itm.gens))
    count = Counter(tmp)
    for c in count.values():
        if c / count_of_chromosomes >= 0.6:
            return True
    return False


def genetic_algorythm(matrix, count_of_vertex):
    matrix: Matrix = Matrix(matrix=matrix, count_of_vertex=count_of_vertex)
    count_of_chromosomes = 300
    chromosomes = [Chromosome(matrix=matrix, parents=False) for _ in range(count_of_chromosomes)]
    chromosomes.sort(key=lambda x: x.distance)

    for _ in range(100):
        chances = selection_chances(chromosomes=chromosomes)
        chromosomes = crossover(chromosomes=chromosomes, chances=chances, matrix=matrix)
        for chrom in chromosomes:
            chrom.mutation()

        chromosomes.sort(key=lambda x: x.distance)

        if check_4_exit(chromosomes, count_of_chromosomes):
            break
    return chromosomes[0].gens, chromosomes[0].distance
