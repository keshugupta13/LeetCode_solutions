# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k == 0:
            return head
    
        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
    
        temp.next = head
        k = k % count
        
        temp = head
        for i in range(k):
            temp = temp.next
            
        head = temp.next
        temp.next = None
        
        return head
        

        
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        