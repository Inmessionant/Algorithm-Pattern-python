class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [float("-inf") for _ in range(n+1)]
        dp[0], dp[1], dp[2] = 0, 0, 1

        for j in range(3, n+1):
            for k in range(j):
                dp[j] = max(dp[j], k * (j-k), k * dp[j-k])

        return dp[n]