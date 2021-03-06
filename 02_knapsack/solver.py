from pyoptim.dynamic_programming import solve_with_dynamic_programming
from pyoptim.helpers import check_solution
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])


def parse_input(input_data):
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count + 1):
        line = lines[i]
        parts = line.split()
        items.append(Item(i - 1, int(parts[0]), int(parts[1])))
    return item_count, capacity, items




def solve_it(input_data):
    item_count, capacity, items = parse_input(input_data)

    value, taken, optimal = solve_with_dynamic_programming(item_count, capacity, items, verbose=1)
    check_solution(items, taken, capacity, value, verbose=1)
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(optimal) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

