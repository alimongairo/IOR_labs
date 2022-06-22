import random


def get_func(n, d, f, x):
    res = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for m in range(n):
                    res += d[i][j]*f[k][m]*x[i][k]*x[j][m]
    return res


def get_x(fact, n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in fact:
        res[i][fact.index(i)] = 1
    return res


def local_search(fact, n, d, f):
    dlb = [0 for _ in range(n)]
    result_list = fact.copy()
    x = get_x(result_list,n)
    result = get_func(n,d,f,x)

    while True:
        for s in range(n):
            flag = 1
            for r in range(n):
                if s != r and dlb[s] == 0 and dlb[r] == 0:
                    delta = 0
                    for k in range(n):
                        if k != s and k != r:
                            delta += 2*(f[s][k] - f[r][k]) * (
                                        d[result_list.index(s)][result_list.index(k)] - d[result_list.index(r)][result_list.index(k)])
                    if (result + delta) < result:
                        result = result - delta
                        idx1 = result_list.index(s)
                        idx2 = result_list.index(r)
                        result_list[idx1], result_list[idx2] = result_list[idx2], result_list[idx1]
                        x = get_x(result_list,n)
                        flag = 0
                        dlb = [0 for _ in range(n)]
            if flag == 1:
                dlb[s] = 1
            else:
                break
            if all(dlb):
                return result_list, result


def perturbation(fact, num):
    idx_list = []
    i = 0
    while i < num:
        tmp1 = random.randint(0,num)
        tmp2 = random.randint(0,num)
        if tmp1 != tmp2:
            idx_list.append((tmp1,tmp2))
            i += 1
    for idx_tuple in idx_list:
        idx1 = fact.index(idx_tuple[0])
        idx2 = fact.index(idx_tuple[0])
        fact[idx1], fact[idx2] = fact[idx2], fact[idx1]
    return fact


def iterated_local_search(fact, n, d, f, tries=10):
    result_list, result = local_search(fact,n,d,f)
    for num in range(2,n+1):
        ptd_list = perturbation(result_list,num)
        tmp, tmp_flow = local_search(ptd_list,len(ptd_list),d,f)
        if tmp_flow < result:
            result = tmp_flow
            result_list = tmp
    return result_list, result
