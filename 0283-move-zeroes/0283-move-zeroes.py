class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        while i < len(nums):
            if nums[i] == 0:
                count += 1
                nums.remove(nums[i])
            i +=1
            if count!= 0:
                nums.append(0)
                count -= 1
