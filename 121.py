from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        demand = 0
        buy = prices[0]
        for sell in prices[1:]:
            if sell > buy:
                demand = max(demand, sell - buy)
            else:
                buy = sell
        return demand


prices = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(prices))
