class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap=[]
        ans = []
        for i in points:
            dist = (i[0] ** 2) + (i[1] ** 2)
            minheap.append([dist,i[0],i[1]])
        heapq.heapify(minheap)
        while k > 0:
            dist , x, y = heapq.heappop(minheap)
            ans.append([x,y])
            k -= 1
        return ans
        