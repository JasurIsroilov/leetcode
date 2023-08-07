from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        res = []
        for i in range(len(s) - 1, -1, -1):
            if s[i] == ' ':
                return len(res)
            res.append(s[i])
        return len(res)


string = ''
s = Solution()
print(s.lengthOfLastWord(string))
