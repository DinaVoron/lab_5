from flask import render_template, request
from app import app
import numpy as np


@app.route('/', methods=['GET'])
def index():
    sub = False
    mul = False
    add = False
    size = 3

    if request.values.get("size"):
        size = int(request.values.get("size"))

    # Узнав размер, строим два массива для матриц
    matrix_first = np.zeros((size, size), dtype=np.int16)
    matrix_second = np.zeros((size, size), dtype=np.int16)

    # Создадим матрицы для результатов
    sub_matrix = np.zeros((size, size), dtype=np.int16)
    mul_matrix = np.zeros((size, size), dtype=np.int16)
    add_matrix = np.zeros((size, size), dtype=np.int16)

    # Построив матрицы, заполняем их значениями
    for i in range(size):
        for j in range(size):
            if request.values.get("1_{}_{}".format(i, j)):
                matrix_first[i][j] = int(request.values.get("1_{}_{}".format(i, j)))
            if request.values.get("2_{}_{}".format(i, j)):
                matrix_second[i][j] = int(request.values.get("2_{}_{}".format(i, j)))

    if request.values.get("sub"):
        sub = True
        np.subtract(matrix_first, matrix_second, sub_matrix)

    if request.values.get("mul"):
        mul = True
        np.dot(matrix_first, matrix_second, mul_matrix)
        print(mul_matrix)

    if request.values.get("add"):
        add = True
        np.add(matrix_first, matrix_second, add_matrix)
        print(add_matrix)

    if request.values.get("reset"):
        size = 3
        sub = False
        mul = False
        add = False
        matrix_first = np.zeros((size, size), dtype=np.int16)
        matrix_second = np.zeros((size, size), dtype=np.int16)

    html = render_template('index.html',
                           size=size,
                           matrix_first=matrix_first,
                           matrix_second=matrix_second,
                           sub=sub,
                           sub_matrix=sub_matrix,
                           mul=mul,
                           mul_matrix=mul_matrix,
                           add=add,
                           add_matrix=add_matrix,
                           len=len)
    return html

