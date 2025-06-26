class Solution:
    def rob(self, nums: List[int]) -> int:
#dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        prev1 = 0  # dp[i - 1]
        prev2 = 0  # dp[i - 2]
        
        for amount in nums:
            temp = prev1
            prev1 = max(prev1, prev2 + amount)
            prev2 = temp
        
        return prev1