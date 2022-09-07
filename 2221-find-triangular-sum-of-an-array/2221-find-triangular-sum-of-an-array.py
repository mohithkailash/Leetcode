class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            n = len(nums)
            for i in range(n-1):
                nums.append((nums[i]+nums[i+1])%10)
            nums = nums[n:]
        return nums[0]