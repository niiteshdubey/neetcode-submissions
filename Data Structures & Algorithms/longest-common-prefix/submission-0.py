class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        strs.sort()
        str1 = strs[0]
        str2 = strs[-1]

        for i in range(min(len(str1), len(str2))):
            if str1[i] != str2[i]:
                return str1[:i]
        return str1