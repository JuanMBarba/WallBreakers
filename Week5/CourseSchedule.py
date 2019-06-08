class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        self.doc = defaultdict(list)
        
        self.memo = {}
        def isCycle(node):
            if self.memo.get(node) != None:
                return self.memo[node]
            elif self.doc[node] == []:
                self.memo[node] = False
                return False
            else:
                for course in self.doc[node]:
                    if self.memo.get(course) != None:
                        if self.memo[course]:
                            return self.memo[course]
                    elif course in self.seen:
                        self.memo[node] = True
                        return True
                    else:
                        self.seen.add(course)
                        if isCycle(course):
                            self.memo[node] = True
                            return True
                
                self.memo[node] = False
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
                if isCycle(item[0]):
                    return False
                    
                
        return True
