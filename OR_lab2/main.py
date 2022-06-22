import algorithms as alg
import time

for i in range(1,8):
    with open(f'test{i}', 'r') as f:
        capacity = int(f.readline())
        weights = list(f.readline().split(sep=' '))
        costs = list(f.readline().split(sep=' '))
        ans = list(f.readline().split(sep=' '))
        num_of_items = len(weights)

        weights = [int(x) for x in weights]
        costs = [int(x) for x in costs]
        ans = [int(x) for x in ans]
        max_cost = 0
        for k in range(num_of_items):
            if ans[k] == 1:
                max_cost += costs[k]

        print(f'     TEST {i}\n')

        st_time = time.time()
        res1, c1, w_tmp = alg.approx(n=num_of_items, w=capacity, weights=weights, costs=costs)
        w1 = capacity - w_tmp
        print(f'2-approx  answer: {ans}')
        print(f'          result: {res1}')
        print(f'          max_cost: {max_cost}')
        print(f'          cost: {c1}')
        print(f'          weight: {w1}')
        print(f'          time: {time.time() - st_time}')
        print(f'          interm_res: ?')
        print()

        st_time = time.time()
        res2 = []
        w2 = 0
        c2 = alg.DP(n=num_of_items, w=capacity, weights=weights, costs=costs)
        print(f'DP        answer: {ans}')
        print(f'          result: {res2}')
        print(f'          max_cost: {max_cost}')
        print(f'          cost: {c2}')
        print(f'          weight: ?')
        print(f'          time: {time.time() - st_time}')
        print(f'          interm_res: {num_of_items * capacity}')
        print()

        # res3 = []
        # w3 = 0
        # c3 = 0
        # alg.BAB(n=num_of_items, c=capacity, weights=weights, costs=costs)
        # print(f'BAB       answer: {ans}')
        # print(f'          result: {res3}')
        # print(f'          max_cost: {max_cost}')
        # print(f'          cost: {c3}')
        # print(f'          weight: {w3}')
        # print()

        st_time = time.time()
        res_tmp, c4, w4 = alg.PTAS(n=num_of_items, c=capacity, weights=weights, costs=costs)
        res4 = [1 if i + 1 in res_tmp else 0 for i in range(num_of_items)]
        print(f'PTAS      answer: {ans}')
        print(f'          result: {res4}')
        print(f'          max_cost: {max_cost}')
        print(f'          cost: {c4}')
        print(f'          weight: {w4}')
        print(f'          time: {time.time() - st_time}')
        print(f'          interm_res: ?')
        print()

        print('\n\n')
