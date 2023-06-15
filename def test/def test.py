numbers = [2, 33, 6, 123, 4, 85, 35, 1, 9, 3]


def sorted_numbers(numbers):
    return list(reversed(sorted(numbers)))
    # return list(map(lambda x: x, (reversed(sorted(numbers)))))


print(sorted_numbers(numbers)) # [123, 85, 35, 33, 9, 6, 4, 3, 2, 1]


###########################################################################

def even_numbers(num):
    return num % 2 == 0


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(lambda x: even_numbers(x), numbers))) #  [2, 4, 6, 8, 10]

