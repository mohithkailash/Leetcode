# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node,up,bottom):
            if node is None:
                return True
            if node.val >= up or node.val <= bottom:
                return False
            return helper(node.left, node.val, bottom) and helper(node.right, up, node.val)
        return helper(root,float(inf),float(-inf))
            
        