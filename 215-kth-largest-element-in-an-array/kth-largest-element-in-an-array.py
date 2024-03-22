
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        numLen = len(nums)
        for i in range(0, numLen):
            if i == numLen - k:
                return heapq.heappop(nums)
            heapq.heappop(nums)