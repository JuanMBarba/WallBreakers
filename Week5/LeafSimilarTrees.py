# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getLeafValue(self, root:TreeNode)->list:
        result = []
        def _dlv(root,result):
            if not root.left and not root.right:
                result.append(root.val)
                return
            if root.left != None:
                _dlv(root.left,result)
            if root.right != None:
                _dlv(root.right,result)
        
        _dlv(root,result)
        
        return result
                
            
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        
        
        return self.getLeafValue(root1) == self.getLeafValue(root2)
