class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.currentCapacity = 0
        
        self.head = ListNode(None)
        self.tail = ListNode(None)
        self.head.next = self.tail
        self.tail.next = self.head
        
        self.map = {}
    
    def addToFront(self, node):
        
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def get(self, key: int) -> int:
        if self.map.get(key) != None:
            self.remove(self.map[key])
            self.addToFront(self.map[key])
            return self.map[key].val[1]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.map.get(key) == None:
            self.map[key] = ListNode((key,value))
            self.addToFront(self.map[key])
            self.currentCapacity +=1
            if self.capacity < self.currentCapacity:
                del self.map[self.tail.prev.val[0]]
                self.remove(self.tail.prev)
        else:
            
            self.map[key].val = (key,value) 
            self.remove(self.map[key])
            self.addToFront(self.map[key])
        
            
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
