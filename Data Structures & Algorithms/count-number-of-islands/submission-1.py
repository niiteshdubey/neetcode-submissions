class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])

        def recur(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            recur(i - 1, j)
            recur(i + 1, j)
            recur(i, j - 1)
            recur(i, j + 1)
        
        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    recur(i, j)
                    res += 1
        return res