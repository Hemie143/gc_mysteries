import cipher
import utils
from copy import deepcopy

koek = '''7 1 13 21 4 2 18 25 6 19 1 3 5 7 9 23 2 4 6 8 24 26 11 12 23 7 8 9 17 10 4 5 6 18 11 11 12 13 10 9 14 13 12 11 10 1 22 19 7 8 4 10 26 21 12 11 6 13 14 6 4 24 5 25 6
9 1 11 19 6 20 10 5 1 25 4 18 19 10 5 2 4 16 24 8 18 9 18 18 9 20 15 10 5 1 1 5 10 20 10 25 10 5 5 20 26 18 10 2 26 9 3 18 12 26 26 25 13 12 24 13 12 11 14 13 11 10 9 19 8
2 3 4 14 5 26 25 24 23 1 17 16 7 6 15 5 9 18 10 25 3 23 24 9 10 7 8 18 16 11 8 6 4 16 2 12 24 9 18 6 21 22 1 2 21 1 5 15 9 19 7 2 11 17 11 12 13 20 10 7 21 11 9 7 5'''

def to_odd_even(k_list):
    result = []
    for l in k_list:
        result.append(['A' if int(c)%2 == 0 else 'B' for c in l])
    return result

def all_bacons(k_list):
    print('**Bacon 1 - No Swap**')
    for line in current_bacon:
        print(cipher.bacon_decrypt(''.join(line), version=1, swapAB=False))
    print('**Bacon 1 - Swap**')
    for line in current_bacon:
        print(cipher.bacon_decrypt(''.join(line), version=1, swapAB=True))
    print('**Bacon 2 - No Swap**')
    for line in current_bacon:
        print(cipher.bacon_decrypt(''.join(line), version=2, swapAB=False))
    print('**Bacon 2 - Swap**')
    for line in current_bacon:
        print(cipher.bacon_decrypt(''.join(line), version=2, swapAB=True))

def list_print_space(k_list):
    for l in k_list:
        print(' '.join(l))

def list_print(k_list):
    for l in k_list:
        print(''.join(l))

koek_msg = koek
koek_list = []
for kl in koek.splitlines():
    koek_list.append(kl.split())

###############################################################################
print('*'*80)
print('Reading per line, from left to right')

current_list = deepcopy(koek_list)
list_print_space(current_list)
current_bacon  = to_odd_even(current_list)
list_print(current_bacon)
all_bacons(current_bacon)

###############################################################################
print('*'*80)
print('Reading per line, from right to left')

current_list = []
for l in koek_list:
    current_list.append(l[::-1])
list_print_space(current_list)
current_bacon = to_odd_even(current_list)
list_print(current_bacon)
all_bacons(current_bacon)

###############################################################################
print('*'*80)
print('Reading per column, from right to left, top to bottom')

current_list = []
num_lines = len(koek_list)
num_chars = len(koek_list[0])
for y in range(num_lines):
    line = []
    for x in range(num_chars):
        c = y * num_chars + x
        yy = c % num_lines
        xx = num_chars - (c // num_lines) - 1
        line.append(koek_list[yy][xx])
    current_list.append(line)
list_print_space(current_list)
current_bacon = to_odd_even(current_list)
list_print(current_bacon)
all_bacons(current_bacon)

###############################################################################
print('*'*80)
print('Reading per column, from right to left, bottom to top')

current_list = []
num_lines = len(koek_list)
num_chars = len(koek_list[0])
for y in range(num_lines):
    line = []
    for x in range(num_chars):
        c = y * num_chars + x
        yy = num_lines - (c % num_lines) - 1
        xx = num_chars - (c // num_lines) - 1
        line.append(koek_list[yy][xx])
    current_list.append(line)
list_print_space(current_list)
current_bacon = to_odd_even(current_list)
list_print(current_bacon)
all_bacons(current_bacon)
