class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def gen(cur, no, nc):
            if(no == 0 and nc == 0):
                result.append(cur)
                return
            if(no > 0):
                gen(cur + "(", no - 1, nc)
            if(no < nc):
                gen(cur + ")", no, nc - 1)
        gen("", n, n)
        return result