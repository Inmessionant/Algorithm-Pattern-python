from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 本题相当于背包里放入数值，那么物品i的重量是nums[i]，其价值也是nums[i]
        if sum(nums) % 2 == 1:  return False
        target = sum(nums) // 2
        # 1.dp[i]表示背包总容量为i，最大可以凑齐i的子集总和为dp[i]
        dp = [0 for _ in range(target + 1)]  # 3.dp初始化

        # 4.确定遍历顺序:如果使用一维dp数组，物品遍历的for循环放在外层，遍历背包的for循环放在内层，且内层for循环倒叙遍历
        for i in range(len(nums)):
            for j in range(target, nums[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])  # 2.递推公式

        if dp[-1] == target:  return True  # 如果dp[i] == i 说明，集合中的子集总和正好可以凑成总和i
        return False


# 回溯
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         if sum(nums) % 2 == 1:  return False
#         target = sum(nums) // 2
#         res = []
#
#         def backpack(start, path, sumpath, target, nums):
#             if sumpath > target or start > len(nums):  return
#             if sumpath == target:
#                 res.append(path[:])
#                 return
#             for i in range(start, len(nums)):
#                 path.append(nums[i])
#                 sumpath += nums[i]
#                 backpack(i + 1, path, sumpath, target, nums)
#                 sumpath -= path.pop()
#
#         backpack(0, [], 0, target, nums)
#         return res
        # return True if res else False


solution = Solution()
nums = [1, 2, 3, 6]
res = solution.canPartition(nums)
print(res)
