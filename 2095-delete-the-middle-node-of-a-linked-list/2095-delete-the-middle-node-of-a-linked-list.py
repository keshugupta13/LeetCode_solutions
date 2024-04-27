# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        if not head:
            return head
        if not head.next:
            return None
        prev = None
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        return head
