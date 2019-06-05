# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        result = [0]
        
        def _sofl(root,result):
            if root:
                if not root.left and not root.right:
                    return True
                if _sofl(root.left,result):
                    result[0] += root.left.val
                
                _sofl(root.right,result)
            return False
        
        _sofl(root,result)
        
        return result[0]
