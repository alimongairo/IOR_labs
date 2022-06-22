import tests

# print('Local Search\n')
# for i in range(1,6):
#     tests.test(i, 'ls')
#     print()

# print('\nIterated Local Search\n')
# for i in range(1,2):
#     tests.test(i, 'ils')
#     print()

res_list = []
for _ in range(20):
    res_list.append(tests.test(1, 'ls'))
    print()
    print(res_list)

# tests.test(0, 'ls')
# tests.test(0, 'ils')
