from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        dp = [1 for _ in range(len(nums))]  # 1.dp[i]表示i之前包括i的最长上升子序列  3.dp初始化
        for i in range(len(nums)):  #4.确定遍历顺序
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)  # 2.递推公式
        return max(dp)