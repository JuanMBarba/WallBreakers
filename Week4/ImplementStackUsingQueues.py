class MyStack:
    def __init__(self):
        from queue import Queue
        """
        Initialize your data structure here.
        """
        self.q = Queue()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.put(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        size = self.q.qsize()-1
        
        while size != 0:
            self.q.put(self.q.get())
            size-=1
            
        return self.q.get()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        size = self.q.qsize()-1
        
        while size != 0:
            self.q.put(self.q.get())
            size-=1
        
        result = self.q.get()
        
        self.q.put(result)
        
        return result
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        
        return self.q.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
