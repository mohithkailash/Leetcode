class Solution:
    def maxArea(self, height: List[int]) -> int:
        i , j = 0 , len(height) - 1
        maxsize = 0
        while i < j:
            minh = min(height[i],height[j])
            cap = minh  * (j-i)
            maxsize = max(maxsize,cap)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxsize
            
        