class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)-1
        while left <= right:
            cur = (left+right) // 2
            count = 0

            count = sum(num <= cur for num in nums)
            if count > cur:
                dupli = cur
                right = cur - 1
            else:
                left = cur + 1
        return dupli