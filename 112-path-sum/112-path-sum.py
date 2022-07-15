# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False
        my_stack = []
        sum = 0
        my_stack.append(root)
        def helper(root,sum):
            removed = my_stack.pop()
            sum += removed.val
            v1 = v2 = False
            if removed.left == None and removed.right == None:
                if sum == targetSum:
                    return True
                return False
            if removed.left:
                my_stack.append(removed.left)
                v1 = helper(removed.left,sum)
            if removed.right:
                my_stack.append(removed.right)
                v2 = helper(removed.right,sum)
            return v1 or v2
        return helper(root,sum)