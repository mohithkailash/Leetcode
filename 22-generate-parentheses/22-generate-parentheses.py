class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def helper(op,clo,string):
            if op == 0 and clo == 0:
                ans.append(string)
                return
            if op == 0:
                for i in range(clo):
                    string += ")"
                ans.append(string)
                return
            if op < clo:
                helper(op-1,clo,string+"(")
                helper(op,clo-1,string+")")
            else:
                helper(op-1,clo,string+"(")
        helper(n,n,"")
        return ans