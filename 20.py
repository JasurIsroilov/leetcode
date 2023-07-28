class Solution:

    def isValid(self, s: str) -> bool:
        stack = []
        for sym in s:
            if stack and sym == ')':
                if stack.pop() != '(':
                    return False
            elif stack and sym == ']':
                if stack.pop() != '[':
                    return False
            elif stack and sym == '}':
                if stack.pop() != '{':
                    return False
            else:
                stack.append(sym)

        return False if stack else True


sol = Solution()
print(sol.isValid('(('))
