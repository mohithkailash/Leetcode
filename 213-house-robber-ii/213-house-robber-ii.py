class Solution:
    def rob(self, nums: List[int]) -> int:
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
        if len(nums) == 1:
            return nums[0]
        dp = [-1] * (len(nums)+2)
        non_zero = helper(1)
        final_value = nums.pop()
        dp = [-1] * (len(nums)+2)
        non_last = nums[0] + helper(2)
        return max(non_zero,non_last)