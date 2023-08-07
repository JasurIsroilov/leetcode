class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in range(len(t)):
            if not s:
                return True
            if t[i] == s[0]:
                s = s[1:]
        return True if not s else False


s = ""
t = "ahbgdc"
sol = Solution()
print(sol.isSubsequence(s, t))
