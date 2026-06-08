class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        
        n = len(nums)
        for val, count in countMap.items():
            if count > n // 2:
                return val
        
        return -1