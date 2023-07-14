class Solution:
    def fib(self, x: int) -> int:
        """
        fib is 1, 1, 2, 3, 5, 8
        :param x:
        :return:
        """

        def recurFib(n, memo):
            if n in memo:
                return memo[n]
            memo[n] = recurFib(n - 1, memo) + recurFib(n - 2, memo)
            return memo[n]

        return recurFib(x, {0: 0, 1: 1, 2: 1})

    def climbStairs(self, n: int) -> int:
        memo = {1: 1, 2: 2}
        if n in memo:
            return memo[n]
        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]
        print(memo)
        return memo[n]


sol = Solution()
ans = sol.climbStairs(6)
print("expect 0, 1:", ans)
