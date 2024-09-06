# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        num_set = set(nums)
        prev = None
        current = head
        while current:
            if current.val in num_set:
                if prev is None:  
                    head = current.next  
                else:
                    prev.next = current.next  

                temp = current 
                current = current.next  
                temp.next = None 
            else:
                prev = current 
                current = current.next  

        return head


        