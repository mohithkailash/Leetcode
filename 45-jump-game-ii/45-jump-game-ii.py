class Solution:
    def jump(self, nums: List[int]) -> int:
        maxi = 0
        count = 0
        currend = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            maxi = max(i+nums[i],maxi)
            if i == currend:
                currend = maxi
                count+=1
        return count
           
            