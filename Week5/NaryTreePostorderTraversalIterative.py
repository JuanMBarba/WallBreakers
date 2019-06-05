# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = [root]
        result = []
        
        if not root:
            return result
        
        while stack:
            while stack[-1].children:
                stack.append(stack[-1].children[0])
                stack[-2].children = stack[-2].children[1:]
            
            result.append(stack.pop().val)
        
        return result
