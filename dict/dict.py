def command(command):
    dict = {}
    product = []
    quantity = []
    new_dict = {}

    while not command == "end":
        current_data = command.split()

        dict[current_data[0]] = int(current_data[1])

        command = input()

    for k, v in dict.items():
        print(f"{k}:{v}")
    print()

    for k in dict.keys():
        product.append(k)
    print(product)
    print()

    for v in dict.values():
        quantity.append(v)
    print(quantity)
    print()

    for el in product:
        new_dict[el] = quantity[0]
        del quantity[0]
    print(new_dict)


command(input())
