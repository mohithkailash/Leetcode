class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        max_size = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[i])
            max_size=max(max_size,len(my_set))
        return max_size
                