class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angMap = defaultdict(list)
        for string in strs:
            angMap["".join(sorted(string))].append(string)
        res = list()
        return list(angMap.values())