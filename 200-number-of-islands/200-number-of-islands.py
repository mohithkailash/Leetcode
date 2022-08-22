class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows , cols = len(grid) , len(grid[0])
        
                    
                    
        def helper(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            helper(i-1,j)
            helper(i+1,j)
            helper(i,j+1)
            helper(i,j-1)
            
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    helper(i,j)
        #print(grid)
        return count