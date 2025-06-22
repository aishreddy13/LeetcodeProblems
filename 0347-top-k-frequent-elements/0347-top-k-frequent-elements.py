import heapq
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = Counter(nums)

        # Step 2: Use a max-heap to get k most frequent
        heap = [(-count, num) for num, count in freq_map.items()]
        heapq.heapify(heap)

        # Step 3: Extract k elements
        result = []
        for _ in range(k):
            count, num = heapq.heappop(heap)
            result.append(num)

        return result
