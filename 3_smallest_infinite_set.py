class SmallestInfiniteSet:

    def __init__(self):
        self.popped = {}
        self.smallest = 1

    def popSmallest(self) -> int:
        for i in range(self.smallest, 1001):
            if not (i in self.popped):
                self.popped[i] = True
                return i
        return i


    def addBack(self, num: int) -> None:
        if self.smallest > num:
            self.smallest = num 
        if num in self.popped:
            del self.popped[num]


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)