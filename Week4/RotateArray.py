class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        from queue import Queue
        
        q = Queue()
        
        for i in nums[::-1]:
            q.put(i)
        
        while k != 0:
            q.put(q.get())
            k-=1
        

        count = 1
        while not q.empty():
            nums[count*-1]=q.get()
            count+=1
