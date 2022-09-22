# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.ans = root.val
        self.maxdiff = sys.maxsize
        def dfs(node):
            if not node:
                return
            diff = abs(node.val - target)
            if diff < self.maxdiff:
                self.ans = node.val
                self.maxdiff = diff
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        dfs(root)
        return self.ans
            
        