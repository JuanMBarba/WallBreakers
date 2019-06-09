class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        values = [0 for x in range(len(graph))]
        
        
        def _iB(x):
            
            for vertex in graph[x]:
                if values[vertex] == values[x]:
                    return False
                elif values[vertex] == 0:
                    values[vertex] = 2 if values[x] == 1 else 1
                    
                    if not _iB(vertex):
                        return False
            
            return True
        
        for x in range(len(graph)):
            if values[x] == 0:
                values[x] = 1
            if not _iB(x):
                return False
        
        
        return True
