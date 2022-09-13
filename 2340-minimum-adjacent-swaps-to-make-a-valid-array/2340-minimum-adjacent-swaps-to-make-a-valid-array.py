class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        minpos = maxpos = 0
        minval = maxval = nums[0]
        for i in range(len(nums)):
            if nums[i] < minval:
                minpos = i
                minval = nums[i]
            if nums[i] >= maxval:
                maxpos = i
                maxval = nums[i]
        left = minpos
        right = len(nums) - (1 + maxpos)
        print(left,maxpos)
        if minpos > maxpos:
            return right + left - 1
        else:
            return right + left