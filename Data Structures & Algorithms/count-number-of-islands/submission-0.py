class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        res = 0
        vis = [[False] * m for _ in range(n)]

        def recur(i, j):
            if i < 0 or j < 0 or i >= n or j >= m or vis[i][j] or grid[i][j] == "0":
                return 
            vis[i][j] = True
            recur(i, j - 1)
            recur(i, j + 1)
            recur(i - 1, j)
            recur(i + 1, j)
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and vis[i][j] == False:
                    recur(i, j)
                    res += 1
        return res
