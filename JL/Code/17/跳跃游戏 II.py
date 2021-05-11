from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:  # 题目说一定能到达
        step, curcover, nextcover = 0, 0, 0  # step维护需要最少的步数 curcover维护当前step步数能到最远的距离，nextcover维护step+1能到最远的距离

        for i in range(len(nums)):
            if i > curcover:
                step += 1
                curcover = nextcover
            nextcover = max(nextcover, i + nums[i])

        return step