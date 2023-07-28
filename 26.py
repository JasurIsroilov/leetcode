from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dummy = []
        j = 0
        for i in range(len(nums)):
            if nums[i] not in dummy:
                nums[j] = nums[i]
                j += 1
            dummy.append(nums[i])
        return j


s = Solution()
nums = [1,1,2]
print(s.removeDuplicates(nums))
print(nums)
