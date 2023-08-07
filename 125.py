class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = list(filter(lambda x: x.isalnum(), s.lower()))
        return new_s[::] == new_s[::-1]


s = ' '
sol = Solution()
print(sol.isPalindrome(s))
