class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [None]*1000000
        

    def add(self, key: int) -> None:
        if self.set[key] == None:
            self.set[key] = key

    def remove(self, key: int) -> None:
        if self.set[key] == key:
            self.set[key] = None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if self.set[key] == key:
            return True
        else:
            return False
