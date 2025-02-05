from collections import Counter 
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)

        for index, value in enumerate(arr):
            if value == arr[index + (length >> 2)]:
                return value
        return 0