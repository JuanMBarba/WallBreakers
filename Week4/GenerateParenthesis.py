class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generateParenthesis2(n: int):
            if n == 0:
                yield ""
                return

            for i in range(n):
                for x in generateParenthesis2(i):
                    for y in generateParenthesis2(n-i-1):
                        yield "(" + x + ")" + y
        
        result = []
        
        for x in generateParenthesis2(n):
            result.append(x)
        
        return result
