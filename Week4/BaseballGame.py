class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        result = 0
        for x in ops:
            try:
                stack.append(int(x))
                result+=int(x)
            except:
                if x == 'C':
                    result -= stack.pop()
                    
                elif x == 'D':
                    value = stack[-1]*2
                    stack.append(value)
                    result+=value
                elif x =='+':
                    value = stack[-1]+stack[-2]
                    stack.append(value)
                    result+=value
        
        return result
