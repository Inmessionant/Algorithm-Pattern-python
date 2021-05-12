from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # +(left) - (right) = target
        # left + right = sum
        # left = (sum + target) // 2

        sumNums = sum(nums)
        if sumNums < target: return 0
        if (sumNums + target) % 2 == 1: return 0
        bagSize = (sumNums + target) // 2

        # 1.dp[j] 表示：填满j（包括j）这么大容积的包，有dp[i]种方法
        # 3.dp数组初始化,dp[0] = 1，装满容量为0的背包，有1种方法，就是装0件物品
        dp = [0 for _ in range(bagSize + 1)]
        dp[0] = 1
        # 4.确定遍历顺序:对于01背包问题一维dp的遍历，nums放在外循环，target在内循环，且内循环倒序
        for i in range(len(nums)):
            for j in range(bagSize, nums[i] - 1, -1):
                dp[j] += dp[j - nums[
                    i]]  # 2.递推公式:不考虑nums[i]的情况下，填满容量为j - nums[i]的背包，有dp[j - nums[i]]中方法,那么只要搞到nums[i]的话，凑成dp[j]就有dp[j - nums[i]]种方法
        return dp[-1]
