class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already = {}
        for i in range(0,len(nums)):
            left_over = target - nums[i]
            if left_over in already:
                return already[left_over],i
            else:
                already[nums[i]] = i