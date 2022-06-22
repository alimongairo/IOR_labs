import local_search as ls
import time
import random


def test(num, key):
    with open(f'qap_test\\test{num}', 'r') as f:
        n = int(f.readline())
        distance = []
        for _ in range(n):
            line = f.readline().split(sep=' ')
            while '' in line:
                line.remove('')
            line[-1] = line[-1].strip('\n')
            distance.append([int(x) for x in line])
        f.readline()
        flow = []
        for _ in range(n):
            line = f.readline().split(sep=' ')
            while '' in line:
                line.remove('')
            line[-1] = line[-1].strip('\n')
            flow.append([int(x) for x in line])

        print(f'N = {n}')
        # print('\nD')
        # for i in range(n):
        #     print(distance[i])
        # print('\nF')
        # for i in range(n):
        #     print(flow[i])
        if key == 'ls':
            st_time = time.time()
            factories = [i for i in range(0, n)]
            random.shuffle(factories)
            res_lst, res = ls.local_search(factories, n, distance, flow)
            fn_time = time.time() - st_time
            print(res_lst)
            print(res)
            print(fn_time)
            return res
        elif key == 'ils':
            st_time = time.time()
            factories = [i for i in range(0, n)]
            random.shuffle(factories)
            res_lst, res = ls.iterated_local_search(factories, n, distance, flow)
            fn_time = time.time() - st_time
            print(res_lst)
            print(res)
            print(fn_time)
            return res
