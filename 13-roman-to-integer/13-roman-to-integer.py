class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        i = 0
        while i < len(s):
            if i == len(s)-1:
                ans += translations[s[i]]
                i += 1
            else:
                if translations[s[i]] < translations[s[i+1]]:
                    ans += translations[s[i+1]] - translations[s[i]]
                    #print(ans)
                    i += 2
                else:
                    ans += translations[s[i]]
                    i += 1
        return ans
                