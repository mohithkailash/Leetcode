class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        count = 0
        def helper(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return 
            isConnected[i][j] = 2
            while j < cols:
                print(i,j)
                if isConnected[i][j] == 1:
                    isConnected[i][j] = 2
                    helper(j,0)
                j += 1
        for i in range(rows):
            for j in range(cols):
                if isConnected[i][j] == 1:
                    count += 1
                    helper(i,j)
        
        return count
                