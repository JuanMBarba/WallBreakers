class Solution:
    def countOfAtoms(self, formula: str) -> str:
        from collections import defaultdict
        
        dd = defaultdict(int)
        
        def parse(pformula: str, multiplier: int):
            
            lpf = len(pformula)
            skip = -1
            for index, letter in enumerate(pformula):
                if index < skip:
                    continue
                if letter.isupper():
                    atom = letter
                    amount = ""
                    for i in range(index+1,lpf):
                        nl = pformula[i]

                        if nl.islower():
                            atom+=nl
                        elif nl.isnumeric():
                            amount += nl
                        else:
                            break
                    if amount == "":
                        dd[atom]+=1*multiplier
                    else:
                        dd[atom]+=int(amount)*multiplier
                
                if letter == "(":
                    lp = 1
                    rp = 0
                    subF = ""
                    mul = ""
                    for i in range(index+1,lpf):
                        
                        if pformula[i] == "(":
                            lp+=1
                        
                        if pformula[i] == ")":
                            rp+=1
                            
                        if lp == rp:
                            for j in range(i+1, lpf):
                                if not pformula[j].isnumeric():
                                    break
                                mul+=pformula[j]
                            skip = i
                            break
                        subF+=pformula[i]
        
                    parse(subF, 1* multiplier if mul == "" else multiplier * int(mul))
        
        parse(formula, 1)
        result = ""
        for x in sorted(dd.items(), key = lambda r: r[0]):
            result+=x[0]+("" if x[1] == 1 else str(x[1]))
            
        return result
