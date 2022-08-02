class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * (len(nums)+2)
        def helper(i):
            if i >= len(nums):
                return 0
            if dp[i+2] == -1:
                dp[i+2] = helper(i+2)
            ans1 = nums[i] + dp[i+2]
            if dp[i+1] == -1:
                dp[i+1] = helper(i+1)
            ans2 = dp[i+1]
            dp[i] = max(ans1,ans2)
            return dp[i]
        #print(dp)
        return helper(0)