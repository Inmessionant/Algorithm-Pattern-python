from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for j in range(len(nums)):
            nums[j] = max(nums[j], nums[j] + nums[j-1])
        return max(nums)


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
res = solution.maxSubArray(nums)
print(res)