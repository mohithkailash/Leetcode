class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        bucket = [-1] * (len(nums)+1)
        mymap = {}
        for i in nums:
            if i not in mymap:
                mymap[i] = 0
            mymap[i] += 1
        for i in mymap:
            if bucket[mymap[i]] == -1:
                bucket[mymap[i]] = [i]
            else:
                bucket[mymap[i]].append(i)
        count = k
        for i in range(len(bucket)-1,-1,-1):
            if count == 0:
                break
            print(i)
            if bucket[i] != -1:
                ans += bucket[i]
                count -= len(bucket[i])
        return ans
                
                