# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if head == None:
            return None
        
        currentNode = head
        
        result = ListNode(currentNode.val)
        
        while currentNode.next != None:
            
            currentNode = currentNode.next
            
            temp = result
            
            result = ListNode(currentNode.val)
            
            result.next = temp
        
        return result
