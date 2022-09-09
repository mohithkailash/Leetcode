class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        premin = nums[0]
        count = 1
        for i in nums[1:]:
            if i > premin + k:
                count += 1
                premin = i
        return count