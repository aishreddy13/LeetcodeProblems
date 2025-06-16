class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # Handle empty list edge case
        
        # Sort the numbers first
        nums = sorted(nums)
        max_count = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue  # Skip duplicates
            elif nums[i] == nums[i - 1] + 1:
                count += 1  # Increment count if consecutive
            else:
                max_count = max(max_count, count)  # Update max_count if the sequence ends
                count = 1  # Reset the count for the new sequence
        
        # Final check after the loop
        return max(max_count, count)