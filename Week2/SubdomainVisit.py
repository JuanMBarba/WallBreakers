class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        from collections import defaultdict
        
        record = defaultdict(int)
        
        
        for domains in cpdomains:
            temp = domains.split()
            for index in range(len(temp[1])):
                if index == 0:
                    record[temp[1]]+=int(temp[0])
                
                elif temp[1][index] == ".":
                    record[temp[1][index+1:]]+=int(temp[0])
        
        return [str(x[1])+' '+ x[0] for x in record.items()]
