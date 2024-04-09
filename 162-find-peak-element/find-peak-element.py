class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2)
            print(l, r, m)
            if nums[m] > nums[l] and nums[m] > nums[r] and r - l == 2:
                return m
            elif nums[m] > nums[l]:
                l += 1
            elif nums[m] > nums[r]:
                r -= 1
            else:
                l += 1
        return l - 1