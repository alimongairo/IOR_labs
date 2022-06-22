import hamilton as alg
import time
import math


def test(num):
    print(f'     TEST {num}')
    if num < 6:
        with open(f'ham_tests\\{num}.tsp', 'r') as f:
            count_of_vertex = int(next(f))
            coordinates = []
            for _ in range(count_of_vertex):
                temp = next(f).split(sep=' ')
                while '' in temp:
                    temp.remove('')
                coordinates.append([float(element) for element in temp])
        matrix = [[0 for _ in range(count_of_vertex)] for _ in range(count_of_vertex)]
        for i in range(count_of_vertex):
            for j in range(count_of_vertex):
                matrix[i][j] = math.sqrt(
                    (coordinates[i][1] - coordinates[j][1]) ** 2 + (coordinates[i][2] - coordinates[j][2]) ** 2)

    else:
        with open(f'ham_tests\\{num}.tsp', 'r') as f:
            count_of_vertex = int(next(f))
            matrix = []
            for _ in range(count_of_vertex):
                temp = next(f).split(sep=' ')
                while '' in temp:
                    temp.remove('')
                matrix.append([float(element) for element in temp])
    st_time = time.time()
    road, distance = alg.genetic_algorythm(matrix=matrix)
    print(f'path: {road}')
    print(f'distance: {distance}')
    print(f'time: {time.time() - st_time}')
    print()
