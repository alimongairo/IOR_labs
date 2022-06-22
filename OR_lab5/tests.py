import time
import genetic_algorythm as alg


def test(file_name, num):
    with open(f'tests\\{file_name}.txt') as f:
        line = f.readline().split(sep=' ')
        m = int(line[0])
        p = int(line[1])
        print(m, p)
        m2p_matrix = [[0 for _ in range(p)] for _ in range(m)]
        for i in range(m):
            line = f.readline().split(sep=' ')
            m_tmp = int(line[0])
            p_tmp = [int(line[i]) for i in range(1,len(line)-1)]
            for j in p_tmp:
                m2p_matrix[m_tmp-1][j-1] = 1
        # for i in range(m):
        #     print(m2p_matrix[i])
        # print()
        ones_count = 0
        p2m_matrix = [[0 for _ in range(m)] for _ in range(p)]
        for i in range(m):
            for j in range(p):
                if m2p_matrix[i][j] == 1:
                    ones_count += 1
                p2m_matrix[j][i] = m2p_matrix[i][j]
        # for i in range(p):
        #     print(p2m_matrix[i])
        p_matrix = [[] for _ in range(p)]
        for i in range(p):
            for j in range(m):
                if p2m_matrix[i][j] == 1:
                    p_matrix[i].append(j)
        # for i in range(m):
        #     print(p_matrix[i])

        p_final_i = [[12, 14, 18], [1, 3, 10, 11, 16, 17], [0, 2, 4, 6, 7, 15], [5, 8, 9, 13, 19], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
        m_final_i = [[4, 9, 10, 13], [2, 11, 12], [1, 14, 15, 16, 17, 19], [0, 3, 5, 6, 7, 8, 18]]
        p_final_a = [[4, 16], [0, 3, 6, 8], [1, 2, 14, 19], [7, 9, 11, 15, 17, 18], [5, 10, 12, 13]]
        m_final_a = [[6, 11, 14], [0, 5, 8, 15, 18, 19], [1, 2, 3, 4, 7], [9, 10, 13], [12, 16, 17]]
        i_res = alg.get_score(p2m_matrix, p_final_i, m_final_i, ones_count)
        a_res = alg.get_score(p2m_matrix, m_final_a, p_final_a, ones_count)
        print(i_res)
        print(a_res)

        # st_time = time.time()
        # p_res, m_res, score = alg.genetic_algorythm(m2p_matrix,p2m_matrix,p_matrix,p,m,ones_count)
        # print(f'TEST   {num}')
        # print(f'p_res: {p_res}')
        # print(f'm_res: {m_res}')
        # print(f'score: {score}')
        # print(f'time:  {time.time()-st_time}')

        # ans_m = [0 for _ in range(m)]
        # for cluster_num, cluster in enumerate(m_res):
        #     for itm_num in cluster:
        #         ans_m[itm_num] = cluster_num + 1
        # ans_p = [0 for _ in range(p)]
        # for cluster_num, cluster in enumerate(p_res):
        #     for itm_num in cluster:
        #         ans_p[itm_num] = cluster_num + 1
        # with open(f'answers\\{file_name}.sol', 'w') as file:
        #     for i in ans_m:
        #         file.write(f'{i} ')
        #     file.write('\n')
        #     for i in ans_p:
        #         file.write(f'{i} ')
