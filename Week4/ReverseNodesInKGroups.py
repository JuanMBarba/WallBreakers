# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        
        def rGroup(head,k):
            if k == 0:
                return head
            if head == None:
                return head
            rGroup(head.next, k-1)          
            head.next.next = head
            head.next = None
            return head
            
        count=1
        newHead = None
        tempHead = head
        nextHead = None
        current = head
        while current != None:
            if count == k:
                if newHead == None:
                    newHead = current
                    
                temp = current.next
                ntHead = rGroup(tempHead, k-1)

                if nextHead != None:
                    nextHead.next = current
                nextHead = ntHead
                tempHead = temp
                current = tempHead
                count = 0
            else:
                current = current.next
            count+=1
            
        if count != 1:
            if nextHead != None:
                
                nextHead.next = tempHead
            else:
                newHead = head
        
        return newHead
            
