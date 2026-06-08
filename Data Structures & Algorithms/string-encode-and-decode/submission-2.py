class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for string in strs:
            res += str(len(string)) + "#" + string
        print(res)
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            cnt = int(s[i:j])  # size of the string
            i = j + 1
            j = i + cnt
            string = s[i:j]
            res.append(string)
            i = j
        return res