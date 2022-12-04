import math
import os
import subprocess


def get_H_num(num_C: int, num_N: int, num_O: int):
    all_seq = []
    if num_C != 0:
        max_H_4_C = num_C * 2 + 2
    else:
        max_H_4_C = 0
    if num_N != 0:
        max_H_4_N = num_N + 2
    else:
        max_H_4_N = 0
    if num_N * num_C != 0:
        max_H_4_CN = max_H_4_C + max_H_4_N - 2
    else:
        max_H_4_CN = max_H_4_C + max_H_4_N
    if num_O > max_H_4_CN:
        return all_seq
    max_H_4_CNO = max_H_4_CN
    max_deg_unsat = math.trunc(max_H_4_CNO / 2)
    for deg_unsat in range(max_deg_unsat + 1):
        num_H = max_H_4_CNO - deg_unsat * 2
        all_seq.append([num_C, num_N, num_O, num_H])
    return all_seq


def get_formular(num_list: list, symbol_list: list):
    a_formula = ''
    for idx, a_num in enumerate(num_list):
        if a_num == 0:
            continue
        if a_num == 1:
            a_formula = a_formula + symbol_list[idx]
        else:
            a_formula = a_formula + symbol_list[idx] + str(a_num)
    return a_formula


tracker = 0
num_sum_CNO = 10
symbol_list = ['C', 'N', 'O', 'H']
for num_C in range(num_sum_CNO + 1):
    max_N = num_sum_CNO - num_C
    for num_N in range(max_N + 1):
        num_O = num_sum_CNO - num_N - num_C
        all_seq = get_H_num(num_C=num_C, num_N=num_N, num_O=num_O)
        for a_seq in all_seq:
            a_formula = get_formular(num_list=a_seq, symbol_list=symbol_list)
            print(a_formula)
            tracker = tracker + 1
print(f'Tracker is {tracker}.')
