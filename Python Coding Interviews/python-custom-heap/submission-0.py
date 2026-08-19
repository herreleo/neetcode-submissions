import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    reversed_custom = []

    for num in nums:
        pair = (-num, num)
        heapq.heappush(heap, pair)
    
    while heap:
        pair = heapq.heappop(heap)
        rev_top = pair[1]
        reversed_custom.append(rev_top)
    
    return reversed_custom 



# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
