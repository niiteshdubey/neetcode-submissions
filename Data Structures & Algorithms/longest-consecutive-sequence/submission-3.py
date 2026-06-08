class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        if len(nums) <= 1:
            return len(nums)
        nums.sort()
        # nums = [2, 3, 4, 5, 10, 20]
        i, j, n = 0, 1, len(nums)
        length = 1
        maxLen = 0
        while j < n:
            if nums[i] == nums[j] - 1:
                length += 1
            else:
                length = 1
            i += 1
            j += 1
            maxLen = max(maxLen, length)
        return maxLen
                

            