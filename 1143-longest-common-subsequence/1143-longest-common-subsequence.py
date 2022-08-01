class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
        def helper(i,j):
            if i == m or j == n:
                return 0
            if text1[i] == text2[j]:
                if dp[i+1][j+1] == -1:
                    ans = helper(i+1,j+1)
                    dp[i+1][j+1] = ans
                    dp[i][j]=ans+1
                else:
                    ans = dp[i+1][j+1]
                    dp[i][j]=ans+1
            else:
                if dp[i+1][j] == -1:
                    ans1 = helper(i+1,j)
                    dp[i+1][j] = ans1
                else:
                    ans1 = dp[i+1][j]
                if dp[i][j+1] == -1:
                    ans2 = helper(i,j+1)
                    dp[i][j+1] = ans2
                else:
                    ans2 = dp[i][j+1]
                ans = max(ans1,ans2)
                if(dp[i][j]==-1):
                    dp[i][j]=ans
            return dp[i][j]
        return helper(0,0)