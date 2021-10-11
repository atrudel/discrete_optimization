import numpy as np
import pandas as pd


def value_with(table, subcapacity, item_no, item):
    return item.value + table[subcapacity - item.weight, item_no - 1]

def value_without(table, subcapacity, item_no):
    return table[subcapacity, item_no - 1]

def trace_back(table, items):
    taken = [0] * len(items)
    subcapacity = table.shape[0] - 1
    item_no = table.shape[1] - 1

    while subcapacity > 0:
        while item_no > 0 and table[subcapacity, item_no-1] == table[subcapacity, item_no]:
            item_no -= 1
        taken[item_no - 1] = 1
        subcapacity -= items[item_no - 1].weight
        item_no -= 1
    return taken


def solve_with_dynamic_programming(item_count, capacity, items, verbose=0, save=True):
    table = np.zeros((capacity + 1, item_count + 1), dtype='int')

    for item_no in range(1, table.shape[1]):
        item = items[item_no - 1]
        for subcapacity in range(table.shape[0]):
            if items[item_no - 1].weight <= subcapacity:
                table[subcapacity, item_no] = max(value_with(table, subcapacity, item_no, item),
                                                  value_without(table, subcapacity, item_no))
            else:
                table[subcapacity, item_no] = value_without(table, subcapacity, item_no)
    if verbose > 0:
        print(table)
    value = table[-1, -1]
    taken = trace_back(table, items)
    optimal = 1
    if save:
        pd.DataFrame(table).to_csv('../02_knapsack/dynamic_table.csv')
    return value, taken, optimal
