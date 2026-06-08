class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones, twos = 0, 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
            else:
                twos += 1
        
        i = 0
        while i < zeros:
            nums[i] = 0
            i += 1
        while i < zeros + ones:
            nums[i] = 1
            i += 1
        while i < zeros + ones + twos:
            nums[i] = 2
            i += 1
        