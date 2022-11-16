import csv
import threading
from time import *
from multiprocessing import Process, Queue
import numpy as np


def print_matrix(matrix):
    for i in matrix:
        print(*i, end='\n')


def element(index , matrix1, matrix2,q):
    i, j = index
    res = 0
    for k in range(len(matrix2)):
        res += matrix1[i][k] * matrix2[k][j]
    return q.put(res)


def read_csvmatrix(name_file):
    matrix = []
    with open(name_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for i in reader:
            i = [int(j) for j in i]
            matrix.append(i)

    return matrix


matrix1 = read_csvmatrix('/Users/kirillanpilov/Test/matrix1.csv')
matrix2 = read_csvmatrix('/Users/kirillanpilov/Test/matrix2.csv')
final = np.zeros((len(matrix1), len(matrix2[0])))

if __name__ == '__main__':
    q = Queue()
    process = []
    for i in range(final.shape[0]):
        for j in range(final.shape[1]):
            p = Process(target=element, args=[(i, j), matrix1,matrix2 , q])
            p.start()
            res = q.get()
            final[i][j] = res
            p.join()
    print("Ответ")
    print(final)
