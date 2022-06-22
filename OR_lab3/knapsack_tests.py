import knapsack as alg
import time


def test(num):
    with open(f'knap_tests\\test{num}', 'r') as f:
        capacity = int(f.readline())
        weights = list(f.readline().split(sep=' '))
        costs = list(f.readline().split(sep=' '))
        ans = list(f.readline().split(sep=' '))
        num_of_items = len(weights)

        weights = [int(x) for x in weights]
        costs = [int(x) for x in costs]
        ans = [int(x) for x in ans]
        max_cost = 0
        max_weight = 0
        for k in range(num_of_items):
            if ans[k] == 1:
                max_cost += costs[k]
                max_weight += weights[k]

        print(f'     TEST {num}')

        st_time = time.time()
        res, cost, weight = alg.genetic_algorythm(w=capacity, weights=weights, costs=costs, num_of_items=num_of_items)
        print(f'answer: {ans}')
        print(f'result: {res}')
        print(f'max_cost:   {max_cost}')
        print(f'max_weight: {max_weight}')
        print(f'cost:       {cost}')
        print(f'weight:     {weight}')
        print(f'time: {time.time() - st_time}')
        print()
