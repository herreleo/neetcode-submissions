from typing import List, Set, Tuple


def grid_to_set(grid: List[List[int]]) -> Set[Tuple[int, int]]:
    grid_set = set()

    #each list is index 0, 1, 2
    #double for loop for second coordinate 

    for x,grids in enumerate(grid):
        # print("x",x)
        for y, subgrid in enumerate(grids):
            # print(y)
            
            if subgrid == 1:
                # print("value", subgrid)
                # print("added", x ,y)
                grid_set.add((x,y))
    
    # print(grid_set)

    return grid_set        



# do not modify below this line

output1 = grid_to_set([[1, 0, 1], [0, 1, 0], [1, 0, 1]])
print(type(output1))
print(sorted(list(output1)))
      
output2 = grid_to_set([[1, 0, 0], [0, 0, 0]])
print(type(output2))
print(sorted(list(output2)))

output3 = grid_to_set([[1, 1, 1], [1, 1, 1]])
print(type(output3))
print(sorted(list(output3)))

output4 = grid_to_set([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
print(type(output4))
print(sorted(list(output4)))
