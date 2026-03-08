# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        if head.next is None:
            return None
        fast = head
        i = 0
        while i < n:
            fast = fast.next
            i += 1
        if fast is None:
            return head.next
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head