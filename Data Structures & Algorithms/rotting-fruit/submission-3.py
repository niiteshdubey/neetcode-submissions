class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q, vis = deque(), set()
        rows, cols = len(grid), len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        maxtime = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j, 0))
                    vis.add((i, j))
        while q:
            i, j, t = q.popleft()
            grid[i][j] = 2
            if t > 0:
                maxtime = max(t, maxtime)
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols or grid[ni][nj] == 0 or (ni, nj) in vis:
                    continue
                q.append((ni, nj, t + 1))
                vis.add((ni, nj))
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        return maxtime