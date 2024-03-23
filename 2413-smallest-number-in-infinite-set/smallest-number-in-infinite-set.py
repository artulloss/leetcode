class SmallestInfiniteSet:

    def __init__(self):
        list = [i+1 for i in range(0,1000)]
        heapq.heapify(list)
        self.values = list
        self.removed = []

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.values)
        self.removed.append(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.removed and num not in self.values:
            self.removed.remove(num)
            heapq.heappush(self.values, num)