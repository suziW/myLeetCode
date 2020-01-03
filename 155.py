class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minRecord = [float('inf')]

    def push(self, x: int) -> None:
        self.stack.append(x)
        if x <= self.minRecord[-1]:
            self.minRecord.append(x)
        print(self.stack, self.minRecord)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minRecord[-1]:
            self.minRecord.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minRecord[-1]

if __name__ == "__main__":
    # Your MinStack object will be instantiated and called as such:
    minStack = MinStack()  #
    minStack.push(-2)   #
    minStack.push(0)    #
    minStack.push(-3)   #
    r1 = minStack.getMin()  #   --> 返回 -3.
    minStack.pop()  #
    r2 = minStack.top()  #      --> 返回 0.
    r3 = minStack.getMin()   #   --> 返回 -2.
    print(r1, r2, r3)
