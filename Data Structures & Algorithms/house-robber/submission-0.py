class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        n = len(nums)
        def util(i):
            if i >= n:
                return 0
            if dp[i] > 0:
                return dp[i]
            else:
                dp[i] = max(nums[i] + util(i + 2), util(i + 1))
            return dp[i]
        return util(0)