numbers = [2, 33, 6, 123, 4, 85, 35, 1, 9, 3]


def sorted_numbers(numbers):
    return list(reversed(sorted(numbers)))
    # return list(map(lambda x: x, (reversed(sorted(numbers)))))


print(sorted_numbers(numbers)) # [123, 85, 35, 33, 9, 6, 4, 3, 2, 1]
