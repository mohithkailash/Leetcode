class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [[3,0]]
        for i in s:
            if stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i,1])
            if stack[-1][1] == k:
                stack.pop()
        ans = ""
        for c,v in stack[1:]:
            ans += c*v
        
        return ans