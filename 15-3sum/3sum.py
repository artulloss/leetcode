class Solution:
    def threeSum(self, n: List[int]) -> List[List[int]]:
        n.sort()
        pairs = []

        if(n[0] == n[1] and n[1] == n[2] and n[0] == 0):
            pairs.append((0,0,0))

        for c in range(len(n) - 2):
            if n[c] == n[c - 1]:
                continue;
            l = c + 1
            r = len(n) - 1
            while l < r:
                sum = n[l] + n[c] + n[r]
                if sum > 0:
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    pairs.append((n[l],n[c],n[r]))
                    l += 1
                    r -= 1
                    while l < r and n[l] == n[l - 1]:
                        l += 1
                    while l < r and n[r] == n[r + 1]:
                        r -= 1
        return pairs