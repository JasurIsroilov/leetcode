class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        head, tail = 0, len(needle)
        for i in range(len(haystack) - tail + 1):
            if needle == haystack[head:tail]:
                return head
            head, tail = head + 1, tail + 1
        return -1


haystack = 'sadbutsad'
needle = 'sad'

s = Solution()
print(s.strStr(haystack=haystack, needle=needle))
