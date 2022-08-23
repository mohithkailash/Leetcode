class MedianFinder:

    def __init__(self):
        self.list = []

    def addNum(self, num: int) -> None:
        self.list.append(num)
        return

    def findMedian(self) -> float:
        self.list = sorted(self.list)
        n = len(self.list)
        mid = n // 2
        if n % 2 == 0:
            ans = (self.list[mid] + self.list[mid-1]) / 2
        else:
            ans = self.list[mid]
        return ans


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()