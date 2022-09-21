class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index = {}
        for i in range(len(wordsDict)):
            if wordsDict[i] not in self.index:
                self.index[wordsDict[i]] = []
            self.index[wordsDict[i]].append(i)
                
        

    def shortest(self, word1: str, word2: str) -> int:
        loc1, loc2 = self.index[word1], self.index[word2]
        l1, l2 = 0, 0
        min_diff = float("inf")

        # Until the shorter of the two lists is processed
        while l1 < len(loc1) and l2 < len(loc2):
            min_diff = min(min_diff, abs(loc1[l1] - loc2[l2]))
            if loc1[l1] < loc2[l2]:
                l1 += 1
            else:
                l2 += 1
        return min_diff
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)