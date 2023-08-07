from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed[:] = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i-1] == flowerbed[i] == flowerbed[i+1]:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False


flowerbed = [1,0,0,0,1]
n = 2
s = Solution()
print(s.canPlaceFlowers(flowerbed, n))
print(flowerbed)
