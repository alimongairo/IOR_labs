import algorithms as alg

t1 = 'aaaaaaaaab'
t2 = 'aaaaaaaaa'
t3 = 'aaaabaaaab'
w = 'ab'


def p(res):
    if res:
        print(f'word start position is {res}')
    else:
        print('no occurrence')


#
# print('   Naive')
# res = alg.naive_search(t1,w)
# p(res)
# res = alg.naive_search(t2,w)
# p(res)
# res = alg.naive_search(t3,w)
# p(res)
#
# print('\n   RK')
# res = alg.RK_search(t1,w)
# p(res)
# res = alg.RK_search(t2,w)
# p(res)
# res = alg.RK_search(t3,w)
# p(res)
#
# print('\n   KMP')
# res = alg.KMP_search(t1,w)
# p(res)
# res = alg.KMP_search(t2,w)
# p(res)
# res = alg.KMP_search(t3,w)
# p(res)

print(ord('а'))
print(ord('б'))
print(ord('a'))
print(chr(1073))
print(ord('я'))
