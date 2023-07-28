class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x
        while left < right - 1:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid
            else:
                left = mid
        return left


x = 145

s = Solution()
print(s.mySqrt(x=x))
