from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = 0
        for i in range(len(nums)):
            if i <= cover:
                cover = max(cover, i + nums[i])
                if cover >= len(nums) - 1:
                    return True
        return False


nums = [2, 3, 1, 1, 4]
solution = Solution()
res = solution.canJump(nums)
print(res)
