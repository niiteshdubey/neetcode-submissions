class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        n = len(nums)
        for num in nums:
            countMap[num] += 1
            if countMap[num] > n // 2:
                return num
        return -1