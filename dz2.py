from random import randrange


def get_numbers_ticket(min, max, quantity):
    if min < 1:
        return []
    if max > 1000:
        return []
    if min > quantity > max:
        return []

    l = []
    while True:
        l.append(randrange(min, max))
        l = list(set(l))
        if len(l) == quantity:
            break
    return l


print(get_numbers_ticket(4, 100, 60))
