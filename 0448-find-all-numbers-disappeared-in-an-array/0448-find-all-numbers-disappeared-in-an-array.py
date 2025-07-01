class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num_set = set(nums)
        n = len(nums) + 1
        res = []
        for num in range(1, n):
            if num not in num_set:
                res.append(num)
        return res