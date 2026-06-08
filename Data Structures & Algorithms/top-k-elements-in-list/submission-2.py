class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Using min heap, we will maintain min heap of only k size
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = []
        for key in count.keys():
            heapq.heappush(heap, (count[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for cnt, val in heap:
            res.append(val)
        return res