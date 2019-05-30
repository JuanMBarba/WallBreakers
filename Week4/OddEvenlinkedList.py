# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        even = head.next
        
        odd = head
        
        evenhead = head.next
        
        current = odd
        
        flip = True
        
        while odd != None and even != None:
            
            if flip:
                flip = False
                odd.next = even.next
                if odd.next != None:
                    odd = odd.next
            else:
                flip = True
                even.next = odd.next
                even = even.next
        
        odd.next = evenhead
        
        return head
