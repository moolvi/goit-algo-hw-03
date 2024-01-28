import random

def get_numbers_ticket(min, max, quantity):
    if (type(min) != int) and (type(max) != int) and (type(quantity) != int):
        return []
    elif min < 1:
        return []
    elif (max > 1000) and (max-min < 1):
        return []
    elif quantity > (max-min):
        return []
    range_min_to_max = [elem for elem in range(min, max)]
    set_generate = set()
    while len(set_generate) != quantity:
        element = random.choice(range_min_to_max)
        set_generate.add(element)
        range_min_to_max.remove(element)
    range_min_to_max = list(set_generate)
    range_min_to_max.sort()
    return range_min_to_max