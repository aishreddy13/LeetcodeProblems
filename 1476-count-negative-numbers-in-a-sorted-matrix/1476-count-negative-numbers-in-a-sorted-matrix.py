class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        row_index, col_index = rows - 1, 0
        count = 0

        while row_index >= 0 and col_index < cols:
            if grid[row_index][col_index] < 0:
                count += cols - col_index
                row_index -= 1
            else:
                col_index += 1
        return count        