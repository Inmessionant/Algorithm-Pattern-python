from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0 for _ in range(len(cost))]
        dp[0], dp[1] = cost[0], cost[1]

        for j in range(2, len(cost)):
            dp[j] = min(dp[j-1], dp[j-2]) + cost[j]

        return min(dp[-1], dp[-2])