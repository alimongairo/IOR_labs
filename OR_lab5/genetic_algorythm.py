import random
import math


def decoding(chromosome, n):
    num_of_cells = math.ceil(chromosome[-1] * n)
    # print(f'num of cells: {num_of_cells}')
    cells = [[] for _ in range(num_of_cells)]
    for i in range(len(chromosome) - 1):
        cell_idx = math.ceil(chromosome[i] * num_of_cells) - 1
        cells[cell_idx].append(i)
        # print(f'cells: {cells}')
    return cells


def crossover(parent_1, parent_2):
    n = len(parent_1)
    r = random.randint(1, n - 1)
    # print(r)
    child_1 = parent_1[0:r] + parent_2[r:n]
    child_2 = parent_2[0:r] + parent_1[r:n]
    return child_1, child_2


def count_chromosomes(gen_len):
    top_num = round(gen_len * 0.2)
    bottom_num = round(gen_len * 0.1)
    cross_num = gen_len - top_num - bottom_num
    if cross_num % 2 == 1:
        bottom_num += 1
    cross_num = cross_num // 2
    # print(gen_len, top_num, bottom_num, cross_num)
    return top_num, cross_num, bottom_num


def selection_chances(generation):
    chances = []
    gen_len = len(generation)
    group1, group2, group3, group4 = [], [], [], []
    for i in range(gen_len):
        if i <= gen_len / 4:
            group1.append(generation[i])
        elif i <= gen_len / 2:
            group2.append(generation[i])
        elif i <= 3 * gen_len / 4:
            group3.append(generation[i])
        else:
            group4.append(generation[i])
    for _ in group1:
        chances.append(0.5 / len(group1))
    for _ in group2:
        chances.append(0.3 / len(group2))
    for _ in group3:
        chances.append(0.15 / len(group3))
    for _ in group4:
        chances.append(0.05 / len(group4))
    return chances


def get_new_generation(generation, chances, top_num, cross_num, bottom_num, m):
    new_generation = []
    for i in range(top_num):
        new_generation.append(generation[i][0])
    for _ in range(cross_num):
        parents = random.choices(population=generation, weights=chances, k=2)
        child_1, child_2 = crossover(parent_1=parents[0][0], parent_2=parents[1][0])
        new_generation.append(child_1)
        new_generation.append(child_2)
    for _ in range(bottom_num):
        new_generation.append([random.random() for _ in range(m + 1)])
    return new_generation


def get_p_final(cells, p_matrix, n, ones_total):
    p_final = [[] for _ in range(n)]
    for i in range(n):
        ff_list = []
        for cell in cells:
            out_detail = len(p_matrix[i])
            out_machine = 0
            for c in cell:
                if c not in p_matrix[i]:
                    out_machine += 1
                else:
                    out_detail -= 1
            ff = (ones_total - out_detail) / (ones_total + out_machine)
            ff_list.append(ff)
        best_cell_idx = ff_list.index(max(ff_list))
        p_final[best_cell_idx].append(i)
    return p_final


def get_score(matrix, p_final, cells, ones_total):
    ones_in = 0
    zeros_in = 0
    for i in range(len(cells)):
        for cell in cells[i]:
            for prod in p_final[i]:
                if matrix[prod][cell] == 1:
                    ones_in += 1
                else:
                    zeros_in += 1
    ones_out = ones_total - ones_in
    score = (ones_total - ones_out) / (ones_total + zeros_in)
    return score


def exit_condition(generation):
    counter = 0
    for i in range(1,len(generation)):
        if generation[i] == generation[0]:
            counter += 1
    if counter >= len(generation)*0.9:
        return True
    return False


def genetic_algorythm(m2p_matrix, p2m_matrix, p_matrix, p, m, ones_total):
    amount_of_chromosomes = 1000
    generation = []
    for _ in range(amount_of_chromosomes):
        generation.append([random.random() for _ in range(m + 1)])
    # while True:
    for _ in range(100):
        decoded_generation = []
        p_final_list = []
        score_list = []
        scores = []
        for i in range(amount_of_chromosomes):
            decoded_generation.append(decoding(generation[i], m))
        for chrom in decoded_generation:
            p_final = get_p_final(cells=chrom, p_matrix=p_matrix, n=p, ones_total=ones_total)
            p_final_list.append(p_final)
            score = get_score(matrix=p2m_matrix, p_final=p_final, cells=chrom, ones_total=ones_total)
            score_list.append(score)
        for i in range(amount_of_chromosomes):
            scores.append((generation[i], score_list[i], decoded_generation[i], p_final_list[i]))
        scores.sort(key=lambda x: x[1], reverse=True)
        chances = selection_chances(generation)
        top, cross, bottom = count_chromosomes(len(generation))
        generation = get_new_generation(generation=scores, chances=chances, top_num=top, cross_num=cross,
                                        bottom_num=bottom, m=m)
        # if exit_condition(generation):
        #     break
    return p_final_list[0], decoded_generation[0], scores[0][1]
