# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lower = 1
        upper = n
        cur = n
        while lower <= upper:
            guessOfN = guess(cur)
            if guessOfN == -1:
                upper = cur - 1
            elif guessOfN == 1:
                lower = cur + 1
            else:
                return cur
            cur = lower + ((upper - lower) // 2)