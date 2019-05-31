class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[0]
        for x in S:
            if x == ")":
                value = stack.pop()
                if value == 0:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(stack.pop()+value*2)
            else:
                stack.append(0)
                
        return stack.pop()
