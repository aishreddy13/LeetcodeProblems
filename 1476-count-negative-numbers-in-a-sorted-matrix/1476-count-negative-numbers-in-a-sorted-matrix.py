class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for gr in grid:
            for num in gr:
                if num < 0:
                    count += 1
            
        return count
        