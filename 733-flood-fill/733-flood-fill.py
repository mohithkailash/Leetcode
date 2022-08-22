class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m , n = len(image) , len(image[0])
        num = image[sr][sc]
        def helper(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] !=num or image[i][j] == color:
                return
            image[i][j] = color
            helper(i+1,j)
            helper(i,j+1)
            helper(i-1,j)
            helper(i,j-1)
        helper(sr,sc)
        return image
            