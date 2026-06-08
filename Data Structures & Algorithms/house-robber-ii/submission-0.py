class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob2(arr):
            r, s = 0, 0
            for n in arr:
                t = max(r + n, s)
                r = s
                s = t
            return s
        return max(nums[0], rob2(nums[1:]), rob2(nums[:-1]))