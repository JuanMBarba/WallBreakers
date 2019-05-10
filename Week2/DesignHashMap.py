class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = []
        self.keys = set()
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        if key not in self.keys:
            self.keys.add(key)
            self.map.append([key,value])
            return None

        for x in self.map:
            if x[0] == key:
                x[1] = value
                break

        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        
        if key not in self.keys:
             return -1
        
        for x in self.map:
            if x[0] == key:
                return x[1]
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        for x in range(len(self.map)):
            try:
                if self.map[x][0] == key:
                    del self.map[x]
                    self.keys.remove(key)
            except:
                pass
