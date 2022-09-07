# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        ans = [root.val]
        def ldfs(node):
            if not node or not node.left and not node.right:
                return
            ans.append(node.val)
            if node.left:
                ldfs(node.left)
            else:
                ldfs(node.right)
        def rdfs(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                rdfs(node.right)
            else:
                rdfs(node.left)
            ans.append(node.val)
        def bdfs(node):
            if not node:
                return
            if node != root and not node.left and not node.right:
                ans.append(node.val)
            bdfs(node.left)
            bdfs(node.right)
        
        
        ldfs(root.left)
        bdfs(root)
        rdfs(root.right)
        return ans