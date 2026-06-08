class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preprod = [n for n in nums]
        postprod = [n for n in nums]

        for i in range(1, len(nums)):
            preprod[i] = preprod[i - 1] * preprod[i]

        for i in range(len(nums) - 2, -1, -1):
            postprod[i] = postprod[i + 1] * postprod[i]
        

        print(preprod)
        print(postprod)
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = postprod[i + 1]
            elif i == len(nums) - 1:
                res[i] = preprod[i - 1]
            else:
                res[i] = preprod[i - 1] * postprod[i + 1]
        return res


        