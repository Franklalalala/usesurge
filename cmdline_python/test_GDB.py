import math
import os
import subprocess
import time
import shutil


def get_H_num(num_C: int, num_N: int, num_O: int):
    all_H_nums = []
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
        return all_H_nums
    max_H_4_CNO = max_H_4_CN
    max_deg_unsat = math.trunc(max_H_4_CNO / 2)
    for deg_unsat in range(max_deg_unsat + 1):
        num_H = max_H_4_CNO - deg_unsat * 2
        all_H_nums.append(num_H)
    return all_H_nums


def set_root():
    os.makedirs(f'test_gdb', exist_ok=True)
    os.makedirs(f'test_info', exist_ok=True)
    return os.path.abspath(f'test_gdb'), os.path.abspath(f'test_info')


def set_sub_workbase(formula: str, gdb_path: str, info_path: str):
    os.chdir(gdb_path)
    os.makedirs(formula)
    sub_gdb_path = os.path.abspath(formula)
    os.chdir(info_path)
    os.makedirs(formula)
    sub_info_path = os.path.abspath(formula)
    return sub_gdb_path, sub_info_path


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

surge_path = r'..\bin\surge.exe'
surge_path = os.path.abspath(surge_path)
cmdline_list = [surge_path, '-S', '-Y', '-B1,2,3,4,5,6,7,8,9']
num_sum_CNO = 4
gdb_path, info_path = set_root()
symbol_list = ['C', 'N', 'O', 'H']
for num_C in range(num_sum_CNO + 1):
    max_N = num_sum_CNO - num_C
    for num_N in range(max_N + 1):
        num_O = num_sum_CNO - num_N - num_C
        all_H_nums = get_H_num(num_C=num_C, num_N=num_N, num_O=num_O)
        if len(all_H_nums) == 0:
            continue
        a_CNO_formular = get_formular(num_list=[num_C, num_N, num_O], symbol_list=symbol_list)
        sub_gdb_path, sub_info_path = set_sub_workbase(formula=a_CNO_formular, gdb_path=gdb_path, info_path=info_path)
        for a_H_num in all_H_nums:
            start_time = time.time()
            #################### Start Run ####################
            if a_H_num == 0:
                a_formula = a_CNO_formular
            else:
                a_formula = a_CNO_formular + 'H' + str(a_H_num)

            cmdline_list.append(a_formula)
            smi_file = a_formula + '.smi'
            cmdline_list.append('-o' + smi_file)
            os.chdir(sub_gdb_path)
            out = subprocess.run(cmdline_list, shell=True, capture_output=True)
            del cmdline_list[-2:]
            #################### Post-process ####################
            if out.returncode != 0:
                continue
            if os.stat(smi_file).st_size == 0:
                os.remove(smi_file)
                continue
            os.chdir(sub_info_path)
            with open(a_formula, 'wb') as f:
                f.write(out.stderr)
            end_time = time.time()
            duration = round(end_time - start_time, 2)
            with open(a_formula, 'a') as f:
                f.write('\nTime:\n'+str(duration)+'s\n')
