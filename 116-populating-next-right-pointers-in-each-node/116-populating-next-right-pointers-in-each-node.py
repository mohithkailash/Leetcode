"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return
        q = deque()
        q.append(root)
        while q:
            rightmost = None
            for _ in range(len(q)):
                cur = q.popleft()
                print(cur.val)
                if cur.right:
                    q.append(cur.right)
                    q.append(cur.left)
                cur.next = rightmost
                rightmost = cur
        return root
                
            