from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(min(strs, key=len))
        for i in range(min_len, 0, -1):
            b = set(map(lambda x: x[:i], strs))
            if len(b) == 1:
                return ''.join(b)
        return ''


s = Solution()
print(s.longestCommonPrefix(["dog", "racecar", "car"]))
