"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        
        else:
            result = []
            for child in root.children:
                result+= self.postorder(child)
            
            result+=[root.val]
            
            return result
