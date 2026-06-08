class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        res = []
        while k > 0:
            k -= 1
            curmax = -1
            curval = -1
            for val, cnt in countMap.items():
                if cnt > curmax:
                    curmax = cnt
                    curval = val
            
            if curmax > 0:
                res.append(curval)
                countMap[curval] = 0
        return res