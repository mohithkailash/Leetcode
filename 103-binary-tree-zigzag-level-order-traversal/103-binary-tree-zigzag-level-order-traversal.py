# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        q = []
        q.append(root)
        while q:
            size,temp = len(q) , []
            for i in range(size):
                node = q.pop(0)
                if node:
                    temp.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(ans) % 2 != 0:
                temp = temp[::-1]
            if temp:
                ans.append(temp)
        return ans