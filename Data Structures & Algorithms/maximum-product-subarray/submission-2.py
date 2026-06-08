class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_glob = float("-inf")
        min_prd = 1
        max_prd = 1
        for num in nums:
            min_prd_new = min_prd * num
            max_prd_new = max_prd * num
            min_prd = min(min_prd_new, max_prd_new, num)
            max_prd = max(min_prd_new, max_prd_new, num)
            max_glob = max(min_prd, max_prd, num, max_glob)
        return max_glob