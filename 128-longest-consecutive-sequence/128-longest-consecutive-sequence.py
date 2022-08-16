class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        maxcount = 0
        myset = set(nums)
        for i in nums:
            if i-1 not in myset:
                curcount = 0
                while i in myset:
                    curcount += 1
                    i += 1
                maxcount = max(maxcount,curcount)
        return maxcount