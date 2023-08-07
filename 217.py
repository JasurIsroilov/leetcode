from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return True if len(set(nums)) != len(nums) else False


nums = [1,1,1,3,3,4,3,2,4,2]
s = Solution()
print(s.containsDuplicate(nums))
