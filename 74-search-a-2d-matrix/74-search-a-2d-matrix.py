class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        down = len(matrix) - 1
        while top <= down:
            midrow = (top+down) // 2
            if matrix[midrow][0] == target:
                return True
            if matrix[midrow][0] > target:
                down = midrow-1
            else:
                top=midrow+1
        
        if (midrow>0 and matrix[midrow][0]>target):
            midrow-=1
        left = 0
        right = len(matrix[0]) -1
        while left <= right:
            midcol = (left+right) // 2
            if matrix[midrow][midcol]  == target:
                return True
            if matrix[midrow][midcol]  > target:
                right = midcol-1
            else:
                left = midcol + 1
        return False