x = lambda a, b: a * b
print(x(int(input()), int(input())))

# x = lambda first, second: first + second
# print(x(input(), input()))

######################################################################################

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]

print(list(filter(lambda x: x % 2 == 0, numbers))) # [2, 4, 6, 8, 10, 12, 14, 16]

######################################################################################

# def check_numbers(num):
#     if num % 2 == 0:
#         return True

#     else:
#         return False


# result = list(filter(check_numbers, numbers))

# print(result)  # [2, 4, 6, 8, 10, 12, 14, 16]
