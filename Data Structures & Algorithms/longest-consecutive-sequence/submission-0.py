class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for num in nums:
            # check if this no is start of the sequence
            if num - 1 not in numset:
                curr = 0
                while num + curr in numset:
                    curr += 1
                    longest = max(longest, curr)
        return longest

