class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [-1] * (1+target)
        dp[0]=1
        def helper(target):
            if dp[target] > -1:
                return dp[target]
            count = 0
            for i in nums:
                if i<= target:
                    count += helper(target - i)
            dp[target] = count
            return dp[target]
        return helper(target)
            