class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        suf = deque([0])
        pre = [0]
        ans = []
        for i in range(1,len(security)):
            if security[i] <= security[i-1]:
                pre.append(pre[-1]+1)
            else:
                pre.append(0)
        for i in range(len(security)-2,-1,-1):
            if security[i] <= security[i+1]:
                suf.appendleft(suf[0]+1)
            else:
                suf.appendleft(0)
        print(pre,suf)
        for i in range(len(security)):
            if pre[i] >= time and suf[i] >= time:
                ans.append(i)
        return ans
                