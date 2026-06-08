class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        preprod = 1
        for i in range(len(nums)):
            res[i] = preprod
            preprod *= nums[i]
        
        postprod = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postprod
            postprod *= nums[i]
        
        return res