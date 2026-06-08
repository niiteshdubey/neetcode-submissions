class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pacmap, atlmap = set(), set()
        
        def dfs(r, c, prevHeight, visit):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visit or heights[r][c] < prevHeight:
                return
            visit.add((r, c))
            dfs(r + 1, c, heights[r][c], visit)
            dfs(r - 1, c, heights[r][c], visit)
            dfs(r, c + 1, heights[r][c], visit)
            dfs(r, c - 1, heights[r][c], visit)

        for r in range(rows):
            dfs(r, 0, heights[r][0], pacmap)
            dfs(r, cols - 1, heights[r][cols - 1], atlmap)

        for c in range(cols):
            dfs(0, c, heights[0][c], pacmap)
            dfs(rows - 1, c, heights[rows - 1][c], atlmap)
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i, j) in pacmap and (i, j) in atlmap:
                    res.append([i, j])
        return res


