import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    
    reversed_heap = []
    reversed_list = []

    for num in nums:
        heapq.heappush(reversed_heap, -num)

    
    while reversed_heap:
        top = -heapq.heappop(reversed_heap)
        reversed_list.append(top)

    return reversed_list





# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
