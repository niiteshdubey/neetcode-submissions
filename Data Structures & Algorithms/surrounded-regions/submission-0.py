class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == 'X' or (r, c) in visited:
                return
            visited.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            if board[r][0] == 'O' and (r, 0) not in visited:
                dfs(r, 0)
            if board[r][cols - 1] == 'O' and (r, cols - 1) not in visited:
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == 'O' and (0, c) not in visited:
                dfs(0, c)
            if board[rows - 1][c] == 'O' and (rows - 1, c) not in visited:
                dfs(rows - 1, c)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = 'X'

        