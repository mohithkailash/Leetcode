class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -math.inf
        curr_sum = -math.inf
        for i in range(len(nums)):
            curr_sum = max(nums[i]+curr_sum,nums[i])
            max_sum = max(max_sum,curr_sum)
        return max_sum