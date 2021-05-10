class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1.dp[i][j]表示从(0,0)出发,到达(i,j)有dp[i][j]条不同的路径
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 3.dp数组初始化，dp[0][i], dp[i][0]都是1
        for i in range(n): dp[0][i] = 1
        for i in range(m): dp[i][0] = 1

        # 4.从左上到右下的遍历顺序
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 2.dp[i][j]只有左边和上边两条方向进入

        return dp[-1][-1]