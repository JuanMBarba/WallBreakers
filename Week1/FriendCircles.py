class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        length = len(M)
        
        friends = [x for x in range(length)]
        
        rank = [0 for x in range(length)]
        
        def find(x):
            if friends[x] != x:
                friends[x] = find(friends[x])
            return friends[x]
            
        def union(x, y):
            x_root = find(x)
            y_root = find(y)
            
            if x_root == y_root:
                return
            
            if rank[x_root] > rank[y_root]:
                friends[y_root] = x_root
            else:
                friends[x_root] = y_root
                if rank[x_root] == rank[y_root]:
                    rank[y_root] = rank[y_root] + 1
        
        for x in range(length):
            for y in range(length):
                if x == y:
                    continue
                if M[x][y] == 1:
                    
                    union(x,y)
        
        return len(set([find(x) for x in range(length)]))
