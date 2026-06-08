class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in uniq: # it is a base value
                curr = 1
                while num + 1 in uniq:
                    curr += 1
                    num += 1
                longest = max(curr, longest)
        return longest