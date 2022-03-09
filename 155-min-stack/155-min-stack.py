class MinStack:

    def __init__(self):
        self.mystack = []
        

    def push(self, val: int) -> None:
        if self.mystack == []:
            self.mystack.append((val,val))
        else:
            minimum = self.mystack[-1][1]
            self.mystack.append((val, min(val, minimum)))

    def pop(self) -> None:
        self.mystack.pop()[0]

    def top(self) -> int:
        return self.mystack[-1][0]

    def getMin(self) -> int:
        return self.mystack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()