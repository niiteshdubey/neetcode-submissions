class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rmap = defaultdict(set)
        cmap = defaultdict(set)
        smap = defaultdict(set)

        for r in range(9):
            for c in range(9):
                digit = board[r][c]
                if digit == ".":
                    continue
                if (digit in rmap[r] or
                    digit in cmap[c] or
                    digit in smap[(r // 3, c // 3)]):
                    return False
                rmap[r].add(digit)
                cmap[c].add(digit)
                smap[(r // 3, c // 3)].add(digit)
        return True