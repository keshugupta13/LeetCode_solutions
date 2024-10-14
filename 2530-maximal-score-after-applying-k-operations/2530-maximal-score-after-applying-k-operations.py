import heapq
import math
class Solution(object):
    def maxKelements(self, nums, k):
        pq = [-num for num in nums]
        heapq.heapify(pq)  
        
        score = 0
        for _ in range(k):
            ele = -heapq.heappop(pq)
            score += ele
            new_value = int(math.ceil(ele / 3.0))
            heapq.heappush(pq, -new_value)
        
        return score


