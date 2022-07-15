# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(t1,t2):
            if t1 == None and t2 == None :
                return True
            if t1 != None and t2 != None:
                if t1.val == t2.val:
                    v1 = helper(t1.left,t2.right)
                    v2 = helper(t1.right,t2.left)
                    return v1 and v2
            else:
                return False
        return helper(root,root)