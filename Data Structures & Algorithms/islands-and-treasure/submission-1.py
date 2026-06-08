class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        inf = 2147483647
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        q, visited = deque(), set()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        while q:
            i, j, d = q.popleft()
            grid[i][j] = d
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= rows or nj >= cols or grid[ni][nj] == -1 or (ni, nj) in visited:
                    continue
                q.append((ni, nj, d + 1))
                visited.add((ni, nj))