# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.result = root.val
        self.depth = 0
        
        def _fblv(root,d):
            if not root.left and not root.right:
                return True
            
            if root.left and _fblv(root.left, d+1):
                if d+1 > self.depth:
                    self.depth = d+1
                    self.result = root.left.val
                
            if root.right and _fblv(root.right, d+1):
                if d+1 > self.depth:
                    self.depth = d+1
                    self.result = root.right.val
                
            
            return False
            
            
        _fblv(root, 0)
        return self.result
