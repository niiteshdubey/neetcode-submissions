class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                x, y = j + 1, len(nums) - 1
                while x < y:
                    summ = nums[i] + nums[j] + nums[x] + nums[y]
                    if summ < target:
                        x += 1
                    elif summ > target:
                        y -= 1
                    else:
                        res.append([nums[i], nums[j], nums[x], nums[y]])
                        x += 1
                        y -= 1
                        while x < y and nums[x] == nums[x - 1]:
                            x += 1
                        while x < y and nums[y] == nums[y + 1]:
                            y -= 1
        return res