class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1 for i in range(n+1)]
        def helper(n, dp):
            if n == 1 or n == 2:
                return n
            if dp[n-1] != -1:
                ans1 = dp[n-1]
            else:
                dp[n-1] = helper(n-1,dp)
                ans1 = dp[n-1]
            if dp[n-2] != -1:
                ans2 = dp[n-2]
            else:
                dp[n-2] = helper(n-2,dp)
                ans2 = dp[n-2]
            dp[n] = dp[n-1] + dp[n-2]
            return dp[n]
        return helper(n,dp)