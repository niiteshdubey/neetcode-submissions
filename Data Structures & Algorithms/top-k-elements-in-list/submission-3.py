class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using bucket sort algorithm
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, cnt in count.items():
            bucket[cnt].append(num)
        res = []
        for i in range(len(nums), 0, -1):   # 1 based numbering
            for num in bucket[i]:
                res.append(num)
                if len(res) == k:
                    return res
        