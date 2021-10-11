def solve_with_baseline(item_count, capacity, items):
    value = 0
    weight = 0
    taken = [0] * len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight
    optimal = 0
    return value, taken, optimal