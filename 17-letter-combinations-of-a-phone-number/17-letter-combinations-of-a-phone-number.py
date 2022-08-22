class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def helper(prev,remain):
            num = remain[0]
            letters = mapping[num]
            if len(prev) == n-1:
                for i in letters:
                    ans.append(prev+i)
                return
            else:
                for i in letters:
                    helper(prev+i,remain[1:])
        if digits == "":
            return
        helper("",digits)
        return ans