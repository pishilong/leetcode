from typing import List

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        size = len(grid)
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]

        for i in range(size):
            for j in range(size):
                increase += min(row_max[i], col_max[j]) - grid[i][j]

        return increase

if __name__ == '__main__':
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    s = Solution()
    result = s.maxIncreaseKeepingSkyline(grid)
    print(result)
