# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        if head is None or head.next is None or head.next.next is None:
            return head
        odd = head
        even = head.next
        evenhead = head.next
        while odd.next is not None and odd.next.next is not None:
            odd.next = odd.next.next
            even.next = even.next.next
            even = even.next
            odd = odd.next
        odd.next = evenhead
        return head