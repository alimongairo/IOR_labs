import algorithms as alg
import time


def pr(r,t,c):
    if r:
        print(f'\tfound on positions {r}')
    else:
        print('\tno occurrence')
    print(f'\ttime: {t}')
    print(f'\tcount: {c}')


for i in range(1,5):
    with open('benchmarks/bad_t_' + str(i) + '.txt','r') as f1:
        text = f1.readline()
        # print(text)
    with open('benchmarks/bad_w_' + str(i) + '.txt','r') as f2:
        word = f2.readline()
        # print(word)
    print(f'# BAD SET {i} #')
    print('Naive algorythm:')
    start_time = time.time()
    res, count = alg.naive_search(text, word)
    pr(res,time.time() - start_time,count)
    print('RK algorythm:')
    start_time = time.time()
    res, count = alg.RK_search(text, word)
    pr(res,time.time() - start_time,count)
    print('KMP algorythm:')
    start_time = time.time()
    res, count = alg.KMP_search(text, word)
    pr(res,time.time() - start_time,count)
    print()

for i in range(1,5):
    with open('benchmarks/good_t_' + str(i) + '.txt','r',encoding='utf8') as f1:
        text = f1.read()
        # print(text)
    with open('benchmarks/good_w_' + str(i) + '.txt','r',encoding='utf8') as f2:
        word = f2.readline()
        # print(word)
    print(f'# GOOD SET {i} #')
    print('Naive algorythm:')
    start_time = time.time()
    res, count_1 = alg.naive_search(text, word)
    pr(res,time.time() - start_time,count_1)
    print('RK algorythm:')
    start_time = time.time()
    res, count_2 = alg.RK_search(text, word)
    pr(res,time.time() - start_time,count_2)
    print('KMP algorythm:')
    start_time = time.time()
    res, count_3 = alg.KMP_search(text, word)
    pr(res,time.time() - start_time,count_3)
    print()
