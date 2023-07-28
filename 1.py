from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums), 1):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


s = Solution()
print(s.twoSum([2,7,11,15], 9))
