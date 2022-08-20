# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        def helper(root,k):
            if root == None:
                return
            if k > len(ans)-1:
                ans.append([root.val])
            else:
                ans[k].append(root.val)
            helper(root.left,k+1)
            helper(root.right,k+1)

        helper(root,0)
        return ans
            
            