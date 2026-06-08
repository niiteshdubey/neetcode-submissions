class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = float("-inf")
        for i in range(len(nums)):
            product = 1
            for j in range(i, len(nums)):
                product *= nums[j]
                max_prod = max(product, max_prod)
        return max_prod