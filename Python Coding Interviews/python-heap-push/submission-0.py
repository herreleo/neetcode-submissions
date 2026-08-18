import heapq
from typing import List


def heap_push(heap: List[int], value: int) -> int:
    heap_to_return = []

    for item in heap:
        heapq.heappush(heap_to_return,item)

    heapq.heappush(heap_to_return,value)
    
    smallest = heap_to_return[0]
    
    
    return smallest


# do not modify below this line
print(heap_push([1, 2, 3], 4))
print(heap_push([1, 2, 3], 0))
print(heap_push([1, 2, 3], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 2))
print(heap_push([4, 6, 7, 8, 12, 9, 10], 5))
