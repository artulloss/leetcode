class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = sorted(potions)
        result = [0] * len(spells)

        def bs(spell):
            l, r = 0, len(potions) - 1
            while l <= r:
                m = l + ((r - l) // 2)
                if potions[m] * spell >= success:
                    r = m - 1
                else:
                    l = m + 1
            return l
            

        for i, spell in enumerate(spells):
            result[i] += len(potions) - bs(spell)

        return result
