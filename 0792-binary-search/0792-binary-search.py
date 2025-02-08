class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        for i, n in enumerate(nums):
            if n == target:
                print(n)
                return i
        return -1
                