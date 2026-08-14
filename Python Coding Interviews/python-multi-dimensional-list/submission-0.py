from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    list_of_max = []
    for sublist in nested_arr:
        highest = 0

        for element in sublist:
            if element > highest:
                highest = element
            
        list_of_max.append(highest)


    return list_of_max 
            


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
