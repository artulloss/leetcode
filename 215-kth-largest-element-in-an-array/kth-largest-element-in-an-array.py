class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        # def printStep(l, m, r, p):
        #     for j, num in enumerate(nums):
        #         num = str(num)
        #         if j == p:
        #             print("[" + num + "]", end="")
        #         elif j == m:
        #             print("{" + num + "}", end="")
        #         elif j == r:
        #             print("{" + num + "]", end="")
        #         elif j == l:
        #             print("[" + num + "}", end="")
        #         else:
        #             print(" " + num + " ", end="")
        #     print()

        def partition(l, r):
            pivot = nums[random.randint(l, r)]
            low, mid, high = l, l, r
            # Three-way partitioning
            while mid <= high:
                # printStep(low, mid, high, pivot)
                if nums[mid] < pivot:
                    nums[low], nums[mid] = nums[mid], nums[low]
                    low += 1
                    mid += 1
                elif nums[mid] > pivot:
                    nums[mid], nums[high] = nums[high], nums[mid]
                    high -= 1
                else:
                    mid += 1
            return low, high  # Return the range of elements equal to the pivot

        def quickSelect(l, r):
            if l <= r:
                low, high = partition(l, r)  # Partition the array into three parts
                if k < low:
                    return quickSelect(l, low - 1)
                elif k > high:
                    return quickSelect(high + 1, r)
                else:
                    return nums[k]  # k is within the range of elements equal to the pivot
            return -1

        return quickSelect(0, len(nums) - 1)