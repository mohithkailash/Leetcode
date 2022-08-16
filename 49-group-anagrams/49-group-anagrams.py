class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mymap = {}
        ans = []
        for i in range(0,len(strs)):
            temp = str(sorted(strs[i]))
            if temp not in mymap:
                mymap[temp] = [i]
            else:
                mymap[temp].append(i)
        for i in mymap:
            temp = []
            temp1 = []
            temp = mymap[i]
            for i in temp:
                temp1.append(strs[i])
            ans.append(temp1)
        return ans