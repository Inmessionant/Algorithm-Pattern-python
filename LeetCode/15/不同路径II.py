from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0  # 左上角开始位置有障碍物
        # 1.dp[i][j] 表示从(0,0)出发到(i,j)位置有多少条不同的路径
        dp = [[0 for _ in range(len(obstacleGrid[0]))] for _ in range(len(obstacleGrid))]
        # 3.dp数组初始化，只有没有障碍物才是1，一旦遇到有障碍物，这个位置及以后都是0
        for i in range(len(obstacleGrid[0])):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                break
        # 4.确定遍历顺序，从左上到右下
        for i in range(len(obstacleGrid)):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = 1
            else:
                break
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]  # 2.递推公式，但是要保证没有障碍物，有障碍物这个位置dp[i][j]=0

        return dp[-1][-1]