class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        res = nums[0]
        for i in nums[1:]:
            if i == res:
                count += 1
            else:
                if count == 0:
                    res = i
                    count = 1
                else:
                    count -= 1
        return res