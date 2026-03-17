class MinStack:
    def __init__(self):
        self.stack = []
        self.sMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.sMin or self.sMin[-1] >= val: self.sMin.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.sMin[-1]: self.sMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sMin[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()