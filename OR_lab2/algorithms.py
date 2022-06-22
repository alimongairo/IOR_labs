import itertools


# 2-approx
def get_max(w, result, weights, costs):
    max = 0
    max_idx = 0
    for i in range(len(weights)):
        if i not in result and weights[i] <= w:
            if costs[i] >= max:
                max = costs[i]
                max_idx = i
    return max, max_idx


def approx(n, w, costs, weights):
    c = 0
    result = []
    prices = []
    for i in range(n):
        prices.append((costs[i] / weights[i], i))
    prices.sort(reverse=True)
    last_w = 0
    last_c = 0
    last_i = 0

    while True:
        if len(prices):
            index = prices[0][1]
            if weights[index] < w:
                result.append(index)
                w -= weights[index]
                c += costs[index]
                prices.pop(0)
                last_w = weights[index]
                last_c = costs[index]
                last_i = index
            else:
                break
        else:
            break

    if len(prices):
        if w == 0:
            result.pop(-1)
            w += last_w
            c -= last_c
            max_cost, max_idx = get_max(w=w, result=result, costs=costs, weights=weights)
            if max_cost > last_c:
                c += costs[max_idx]
                w -= weights[max_idx]
                result.append(max_idx)
            else:
                c += last_c
                w -= last_w
                result.append(last_i)
        else:
            min_weight = 99999999999
            for i in range(len(weights)):
                if i not in result and weights[i] < min_weight:
                    min_weight = weights[i]
            if min_weight <= w:
                max_cost, max_idx = get_max(w=w, result=result, costs=costs, weights=weights)
                c += costs[max_idx]
                w -= weights[max_idx]
                result.append(max_idx)
            else:
                result.pop(-1)
                w += last_w
                c -= last_c
                max_cost, max_idx = get_max(w=w, result=result, costs=costs, weights=weights)
                if max_cost > last_c:
                    c += costs[max_idx]
                    w -= weights[max_idx]
                    result.append(max_idx)
                else:
                    c += last_c
                    w -= last_w
                    result.append(last_i)
    return result, c, w


# DP
def DP(n, w, costs, weights):
    bag = [[0 for _ in range(w + 1)] for _ in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i == 0 or j == 0:
                bag[i][j] = 0
            elif j >= weights[i-1]:
                bag[i][j] = max(bag[i-1][j], bag[i-1][j - weights[i-1]] + costs[i-1])
            else:
                bag[i][j] = bag[i - 1][j]
    # print(bag)
    return bag[-1][-1]


# BORDERS AND BOUNDS
def BAB(n, c, weights, costs):
    return []
# ничего не понятно, но очень интересно)))))


# PTAS
def GS(n, c, costs, weights, subset, sum):
        res_num = []
        available = c - sum
        res_cost = 0
        for j in range(1, n):
            if j not in subset and weights[j - 1] <= available:
                res_cost += costs[j - 1]
                available -= weights[j - 1]
                res_num.append(j)
        return res_cost, tuple(res_num)


def PTAS(n, c, costs, weights):
    total_cost = 0
    result = []
    m = []
    sum_w = 0
    for k in range(1, n):
        for j in itertools.combinations([i for i in range(1, n + 1)], r=k):
            m.append(j)
    for subset in m:
        sum_w = 0
        sum_c = 0
        for n in subset:
            sum_w += weights[n - 1]
            sum_c += costs[n - 1]
        if sum_w <= c:
            added_costs, added_tuple = GS(n, c, costs, weights, subset, sum_w)
            if added_costs + sum_c > total_cost:
                total_cost = added_costs + sum_c
                result = []
                for i in subset:
                    result.append(i)
                for j in added_tuple:
                    result.append(j)
    return result, total_cost, sum_w

