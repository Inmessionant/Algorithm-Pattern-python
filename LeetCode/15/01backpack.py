class Solution:
    def backpack(self, weight, value, bagweight):
        dp = [[0 for _ in range(bagweight + 1)] for _ in range(len(weight))]

        for j in range(bagweight, weight[0] - 1, -1):
            dp[0][j] = dp[0][j - weight[0]] + value[0]

        for i in range(len(weight)):
            for j in range(bagweight + 1):
                if j < weight[i]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
        return dp[-1][-1]


    def backpack2(self, weight, value, bagweight):
        dp =

        return dp[-1]



weight = [2, 3, 8]
value = [2, 5, 8]
bagweight = 10
solutin = Solution()
res = solutin.backpack2(weight, value, bagweight)
print(res)