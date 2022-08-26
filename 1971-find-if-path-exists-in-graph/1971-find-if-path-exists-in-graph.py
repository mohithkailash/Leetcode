class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = [0] * (n)
        adj = {}
        for i in edges:
            if i[0] not in adj:
                adj[i[0]] = []
            adj[i[0]].append(i[1])
            if i[1] not in adj:
                adj[i[1]] = []
            adj[i[1]].append(i[0])
        def helper(sv):
            if sv == destination:
                return True
            visited[sv] = 1
            ans = False
            for i in adj[sv]:
                    if visited[i] == 0:
                        ans = ans or helper(i)
                        print(ans)
            return ans
            
        print(len(visited))
        return helper(source)
            