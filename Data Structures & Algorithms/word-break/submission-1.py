class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = [False] * (n + 1)
        memo[n] = True
        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= n and s[i : i + len(w)] == w:
                    memo[i] = memo[i + len(w)]
                if memo[i]:
                    break
        return memo[0]