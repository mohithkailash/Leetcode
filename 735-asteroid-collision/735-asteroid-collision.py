class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0: s.pop()
                elif s[-1] + a > 0: break    
                else: s.pop(); break
            else: s.append(a)        
        return s
                    
        
        # prev = asteroids[-1]
        # for i in range(len(asteroids),-1,-1):
        #     if prev * asteroids[i] > 0:
        #         prev =9