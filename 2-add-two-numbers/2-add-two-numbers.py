# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        carry_val = 0
        curr1 , curr2 = l1 , l2
        head = curr = ListNode()
        while curr1 or curr2:
            temp1 = temp2 = 0
            if curr1 != None:
                temp1 = curr1.val
            if curr2 != None:
                temp2 = curr2.val
            ans = temp1 + temp2 + carry_val
            if ans > 9:
                d1 , carry_val = ans % 10 , ans // 10
            else:
                d1 , carry_val = ans , 0
            curr.next = ListNode(d1)
            curr = curr.next
            if curr1:
                curr1 = curr1.next
            if curr2:
                curr2 = curr2.next
        if carry_val != 0:
            curr.next = ListNode(carry_val)
        return head.next