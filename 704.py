from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        head, tail = 0, len(nums)
        while head < tail:
            mid = (head + tail) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                tail = mid
            else:
                head = mid + 1
        return -1



nums = [5]
target = 5

s = Solution()
print(s.search(nums, target))
