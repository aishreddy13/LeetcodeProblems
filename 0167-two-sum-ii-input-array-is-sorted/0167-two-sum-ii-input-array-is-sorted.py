class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        addi = 0
        i, j = 0, len(numbers)-1

        while i < j:
            addi = numbers[i] + numbers[j]
            if addi < target:
                i += 1
            elif addi > target:
                j -= 1
            elif addi == target:
                return [i+1, j+1]