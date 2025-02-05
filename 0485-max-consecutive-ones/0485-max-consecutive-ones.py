class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_1 = 0
        sum_1 = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                sum_1 +=1
            else:
                sum_1 = 0
            longest_1 = max(sum_1, longest_1) 
        return longest_1    