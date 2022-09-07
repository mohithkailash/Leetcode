class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            n = len(nums)
            temp = []
            for i in range(n-1):
                temp.append((nums[i]+nums[i+1])%10)
            nums = temp
        return nums[0]