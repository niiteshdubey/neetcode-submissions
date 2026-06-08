class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [0] * len(nums)
        sufprod = [0] * len(nums)
        
        product = [0] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod = prod * nums[i]
            preprod[i] = prod
        
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            prod = prod * nums[i]
            sufprod[i] = prod
        
        for i in range(len(nums)):
            if i == 0:
                product[i] = sufprod[i + 1]
            elif i == len(nums) - 1:
                product[i] = preprod[i - 1]
            else:
                product[i] = preprod[i - 1] * sufprod[i + 1]
        return product