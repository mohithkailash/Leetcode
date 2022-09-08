class Solution:
    def minSwaps(self, s: str) -> int:
        def countSwaps(ch):
            count  = 0
            for c in s[::2]:
                if(c != ch):
                    count += 1
            
            return count
            
        c0, c1 = s.count('0'), s.count('1')
        
        if(c0 == c1):
            return min(countSwaps('0'), countSwaps('1'))
        
        if(c0 == c1+1):
            return countSwaps('0')
        
        if(c1 == c0+1):
            return countSwaps('1')
        
        return -1
            