# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
     def reverse(self,head):
        prev = None
        current = head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        return  prev 

     def isPalindrome(self, head):
        if head is None or head.next is None:
            return True
        
        slow= head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
         
        new_head = self.reverse(slow.next)
        
        first = head
        second= new_head
        result = True
        while second is not  None:
             if(first.val != second.val):
                 result = False
                 break
             first = first.next
             second = second.next
            
        self.reverse(new_head)
        return result

            
        """
        :type head: ListNode
        :rtype: bool
        """
        