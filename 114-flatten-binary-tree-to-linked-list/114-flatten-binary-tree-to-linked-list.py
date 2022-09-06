# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(node):
            if not node:
                return
            if not node.right and not node.left:
                return node
            lefttail = dfs(node.left)
            righttail = dfs(node.right)
            
            if lefttail:
                lefttail.right = node.right
                node.right = node.left
                node.left = None
            return righttail if righttail else lefttail
        dfs(root)