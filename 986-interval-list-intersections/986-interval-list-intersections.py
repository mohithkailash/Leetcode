class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        m = len(firstList) 
        n = len(secondList) 
        i = 0
        j = 0
        while i < m and j < n:
            if firstList[i][1] < secondList[j][0]:
                #ans.append(firstList[i])
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                #ans.append(secondList[j])
                j += 1
            else:
                if firstList[i][1] > secondList[j][1]:
                    ans.append([max(firstList[i][0] , secondList[j][0]), secondList[j][1]])
                    j += 1
                else:
                    ans.append([max(firstList[i][0] , secondList[j][0]), firstList[i][1]])
                    i += 1
        return ans
                
        