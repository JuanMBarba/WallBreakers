# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        if not root or (not root.left and not root.right):
            return 0
        
        result2 = [0]
        def depth(root,result,result2):
            
            if not root:
                return result
            
            left = depth(root.left,result+1,result2) 
            right = depth(root.right, result+1,result2)
            if (left-(result+1))+(right-(result+1))>result2[0]:
                result2[0]= (left-(result+1))+(right-(result+1))
            
            return max(left,right)
    
        return max(depth(root.left, 0,result2) + depth(root.right,0,result2), result2[0])
