class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r)//2
            m_val = nums[mid]
            if m_val == target:
                return mid
            elif m_val < target:
                l =mid +1
            elif m_val > target:
                r = mid -1
        return -1