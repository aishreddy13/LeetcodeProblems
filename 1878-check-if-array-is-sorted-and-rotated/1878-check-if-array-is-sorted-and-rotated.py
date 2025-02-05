class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0

        for i, value in enumerate(nums):
            if nums[i-1] > value:
                count += 1
        
        return count <= 1
        
            