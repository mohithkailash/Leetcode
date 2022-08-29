class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mr = 0
        n = len(nums)
        for i in range(0,n):
            if i > mr:
                return False
            mr = max(mr,nums[i]+i)
        return True
        