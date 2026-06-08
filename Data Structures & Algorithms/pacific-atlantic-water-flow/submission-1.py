class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, vis, ph):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in vis or heights[r][c] < ph:
                return
            
            vis.add((r, c))
            dfs(r - 1, c, vis, heights[r][c])
            dfs(r + 1, c, vis, heights[r][c])
            dfs(r, c - 1, vis, heights[r][c])
            dfs(r, c + 1, vis, heights[r][c])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])
        
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
