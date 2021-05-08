class Solution:
    def fib(self, n: int) -> int:
        if n < 2: return n
        k = 2
        # base case
        res = [0, 1]
        # 状态转移
        while k <= n:
            res[0], res[1] = res[1], res[0] + res[1]
            k += 1
        return res[1]