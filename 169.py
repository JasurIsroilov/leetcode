from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        med = int(len(nums)/2)
        elems = set(nums)
        for elem in elems:
            if nums.count(elem) > med:
                return elem
        return -1


nums = [2,2,1,1,1,2,2]
sol = Solution()
print(sol.majorityElement(nums))
