from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        counter = 0
        while 0 in nums:
            nums.remove(0)
            counter += 1
        nums.extend([0]*counter)


nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)
