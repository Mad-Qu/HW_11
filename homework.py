from random import choice


def some_random_bool(amount: int) -> list:
    result_list = []

    for _ in range(amount):
        result_list.append(choice([False, True]))
    return result_list


print(some_random_bool(10))
