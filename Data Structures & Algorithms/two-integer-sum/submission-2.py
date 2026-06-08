class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lkup = {}
        for i in range(len(nums)):
            if target - nums[i] in lkup:
                return [lkup[target - nums[i]], i]
            lkup[nums[i]] = i
        return [-1, -1]