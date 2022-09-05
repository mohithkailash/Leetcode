class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        ans=0
        start=0
        dic={}
        for i in range(len(s)):
            dic[s[i]]=i
            if len(dic)>k:
                start=min(dic.values())+1
                del dic[s[start-1]]
            ans=max(ans,i-start+1)
        return ans
        # i , j = 0 , 0
        # ans = 0
        # check = {}
        # while i < len(s) and j < len(s):
        #     if s[j] not in check:
        #         check[s[j]] = 0
        #     check[s[j]] += 1
        #     while len(check) > k:
        #         check[s[i]] -= 1
        #         if check[s[i]] == 0:
        #             del check[s[i]]
        #         i += 1
        #     ans = max(ans, j-i+1)
        #     j += 1
        # return ans
            
            