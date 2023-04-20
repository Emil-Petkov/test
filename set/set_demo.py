# import time
#
# # this is a list
# ll = [i for i in range(1, 1025 * 32)]
#
# result = False
# start = time.time()
# for el in ll:
#     result = el in ll
# end = time.time()
# print("This is a list ", end - start)  # needed time for iteration: ~3.9302210807800293
#
# ############################################################
#
# # this is a set
# ss = set(ll)
#
#
# start = time.time()
# for el in ss:
#     result = el in ss
# end = time.time()
# print("This is a set: ", end - start)  # needed time for iteration: ~0.0030007362365722656


########################################################################################################################

# ss = {"a", 1, True}  # set definition with method set() 'ss = set()' or curly brackets
# aa = ss
#
# print(type(aa)) # <class 'set'>

########################################################################################################################

# Създаване на множества
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
#
# # Добавяне на елемент към множество
# set1.add(6)
# print(set1)  # Изход: {1, 2, 3, 4, 5, 6}
#
# # Премахване на елемент от множество
# set1.remove(3)
# print(set1)  # Изход: {1, 2, 4, 5, 6}
#
# # Обединение на множества
# set3 = set1.union(set2)
# print(set3)  # Изход: {1, 2, 4, 5, 6, 7, 8}
#
# # Сечение на множества
# set4 = set1.intersection(set2)
# print(set4)  # Изход: {4, 5}
#
# # Разлика на множества
# set5 = set1.difference(set2)
# print(set5)  # Изход: {1, 2, 6}
#
# # Симетрична разлика на множества
# set6 = set1.symmetric_difference(set2)
# print(set6)  # Изход: {1, 2, 6, 7, 8}

########################################################################################################################

# print("LIST")
# list_comprehension = [x % 2 for x in range(1, 11)]
# print(type(list_comprehension))  # <class 'list'>
# print(list_comprehension)  # [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
#
# print("\nSET")
# set_comprehension = {x % 2 for x in range(1, 11)}
# print(type(set_comprehension))  # <class 'set'>
# print(set_comprehension)  # {0, 1} only unique values

########################################################################################################################













