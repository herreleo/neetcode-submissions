def add_two_numbers() -> int:
    sumu = 0

    inpt = input()

    string_input = inpt.split(",")

    int_list = []

    for stint in string_input:
        int_list.append(int(stint))

    for num in int_list:
        sumu += num

    return sumu

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
