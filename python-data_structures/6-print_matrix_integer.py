#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            print("{:d}".format(i[j]), end="")
            if j < len(i) - 1:
                print(" ", end="")
        print("")
