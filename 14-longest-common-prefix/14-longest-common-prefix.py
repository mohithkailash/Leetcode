class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prev = strs[0]
        for i in strs:
            temp = i
            val = min(len(i),len(prev))
            while prev[:val] != i[:val]:
                val -= 1
            prev = prev[:val]
        return prev
                
            