class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i = 0
        for i in range(min(len(word1), len(word2))):
            res.append(word1[i])
            res.append(word2[i])
        if word1[i+1:]:
            res.append(word1[i+1:])
        if word2[i+1:]:
            res.append(word2[i+1:])
        return ''.join(res)


word1 = 'abc'
word2 = 'p'
s = Solution()
print(s.mergeAlternately(word1, word2))
