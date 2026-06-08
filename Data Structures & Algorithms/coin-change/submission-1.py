class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt == 0:
                return 0
            if amt in memo:
                return memo[amt]
            res = 1e9
            for coin in coins:
                if amt - coin >= 0:
                    res = min(res, 1 + dfs(amt - coin))
            memo[amt] = res
            return res
        minCoins = dfs(amount)
        return minCoins if minCoins != 1e9 else -1
