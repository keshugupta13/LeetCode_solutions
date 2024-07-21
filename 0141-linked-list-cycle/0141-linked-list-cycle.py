# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        return False
