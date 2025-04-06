class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if(not digits):
            return []

        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        combos = []
        lenDigits = len(digits)

        def findCombos(str, index):
            if(index >= lenDigits):
                combos.append(str)
                return
            cur = digits[index]
            curLetters = table[cur]
            for ch in curLetters:
                findCombos(str + ch, index + 1)

        findCombos("", 0)
        return combos