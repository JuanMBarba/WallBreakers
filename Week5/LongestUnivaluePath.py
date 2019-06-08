# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        result = [0]
        
        def _lup(root,result):
            
            if not root:
                return 0
            
            else:
                leftpath = 0
                rightpath = 0
                
                left = _lup(root.left,result)
                right = _lup(root.right,result)
                
                if root.left and root.val == root.left.val:
                    leftpath = left + 1
                    
                if root.right and root.val == root.right.val:
                    rightpath =right + 1
                
                result[0] = max(result[0], leftpath + rightpath)
                
                return max(leftpath, rightpath)
        
        _lup(root,result)
        
        return result[0]
