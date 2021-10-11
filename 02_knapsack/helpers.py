class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def failure(message):
    return bcolors.FAIL + message + bcolors.ENDC

def check_solution(items, taken, capacity, solution_value, verbose=0):
    total_weight = 0
    total_value = 0

    print("=" * 80)
    print("Solution detail: \n")
    for i, item in enumerate(items):
        if taken[i] == 1:
            total_weight += item.weight
            total_value += item.value
            if verbose > 0:
                print(f"Item {i+1}: poids {item.weight}, val: {item.value}")
    print(f"Poids total: {total_weight}")

    if total_value != solution_value:
        print(failure(f"Total value doesn not add up: {total_value} != {solution_value}"))
    if total_weight > capacity:
        print(failure(f"EXCEEDS MAX CAPACITY: {capacity}"))
    print("=" * 80)