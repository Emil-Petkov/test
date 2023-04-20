tuple_demo = (
    [1, 2, 3, 4, 5],
    {"banana": 4, "apple": 2, "kiwi": 1},
    (9, 8, 7)
)

print(tuple_demo)  # ([1, 2, 3, 4, 5], {'banana': 4, 'apple': 2, 'kiwi': 1}, (9, 8, 7))

tuple_demo[0][3] = 444444444444  # ([1, 2, 3, 444444444444, 5], {'banana': 4, 'apple': 2, 'kiwi': 1}, (9, 8, 7))

print(tuple_demo)

tuple_demo[1]["hello"] = "world" # ([1, 2, 3, 444444444444, 5], {'banana': 4, 'apple': 2, 'kiwi': 1, 'hello': 'world'}, (9, 8, 7))

print(tuple_demo)

del tuple_demo[1]["banana"] # remove key banana -> ([1, 2, 3, 444444444444, 5], {'apple': 2, 'kiwi': 1, 'hello': 'world'}, (9, 8, 7))

print(tuple_demo)

tuple_demo[0].append(9999) # ([1, 2, 3, 444444444444, 5, 9999], {'apple': 2, 'kiwi': 1, 'hello': 'world'}, (9, 8, 7))

print(tuple_demo)
