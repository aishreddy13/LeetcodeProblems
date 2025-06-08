class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)-1
        numsleng = 0

        while k >= 0:
            if nums[k] != val:
                numsleng += 1
            else:
                nums.remove(nums[k])
            k -= 1
        
        return numsleng
