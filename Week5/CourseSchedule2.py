class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        self.doc = defaultdict(list)
        self.priority = defaultdict(int)
        self.memo = {}
        def isCycle(node,priority):
            if self.doc[node] == []:
                self.priority[node] = max(self.priority[node], priority)
                #self.memo[node] = False
                return False
            else:
                for course in self.doc[node]:
                    
                    if course in self.seen:
                        #self.memo[node] = True
                        return True
                    else:
                        self.seen.add(course)
                        if isCycle(course, priority+1):
                            #self.memo[node] = True
                            return True
                        self.seen.remove(course)
                
                self.priority[node] = max(self.priority[node], priority)
                #self.memo[node] = False
                return False
        
        for x in prerequisites:
            self.doc[x[0]].append(x[1])
            self.doc[x[1]] = self.doc[x[1]]
        
        
        for item in self.doc.items():
            if item[1] == []:
                continue
            else:
                self.seen = set()
                self.seen.add(item[0])
                if isCycle(item[0], self.priority[item[0]]):
                    return []
                    
        result = sorted(self.priority.keys(), key = lambda x : self.priority[x], reverse = True)
        
        if len(result) != numCourses:
            for i in range(numCourses):
                if i not in result:
                    result.append(i)
        return result
