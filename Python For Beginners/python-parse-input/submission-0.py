from typing import List

def read_integers() -> List[int]:
    inpt = input()
    
    string_list = inpt.split(",")

    int_list = []

    for stint in string_list:
        int_list.append(int(stint))

    return int_list

    
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
