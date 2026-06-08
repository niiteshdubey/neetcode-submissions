class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ < 0:
                    j += 1
                elif summ > 0:
                    k -= 1
                else:
                    triplets.add((nums[i], nums[j], nums[k]))
                    j += 1
        res = []
        for tupl in triplets:
            res.append(list(tupl))
        return res