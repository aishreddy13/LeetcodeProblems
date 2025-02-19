from typing import List

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        for index, interval in enumerate(intervals):
            interval.append(index)  # Append original index to keep track

        intervals.sort()  # Sort by start times
        n = len(intervals)
        ans = [-1] * n

        def binary_search(target):
            """Find the smallest index where intervals[index][0] >= target."""
            low, high = 0, n
            while low < high:
                mid = low + (high - low) // 2
                if intervals[mid][0] >= target:
                    high = mid  # Move left
                else:
                    low = mid + 1  # Move right
            return low

        for _, end, org_index in intervals:
            right_index = binary_search(end)
            if right_index < n:
                ans[org_index] = intervals[right_index][2]

        return ans

        