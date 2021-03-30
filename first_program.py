import numpy as np
import time


def mean_of_array(some_array=None):
    print('Calculatin mean')
    time.sleep(1)
    if some_array:
        print(f'Mean equals {round(np.mean(some_array), 3)}')
    else:
        print('Nothing to calculate, lol')


def var_of_array(some_array=None):
    print('Calculatin var')
    time.sleep(1)
    if some_array:
        print(f'Var equals {round(np.var(some_array), 3)}')
    else:
        print('Nothing to calculate, lol')

