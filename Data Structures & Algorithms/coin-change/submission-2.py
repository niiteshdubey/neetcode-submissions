class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount + 1] * (amount + 1)
        memo[0] = 0
        for amt in range(1, amount + 1):
            for c in coins:
                if amt - c >= 0:
                    memo[amt] = min(memo[amt], 1 + memo[amt - c])
        return memo[amount] if memo[amount] != (amount + 1) else -1