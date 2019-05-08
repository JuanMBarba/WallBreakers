class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        
        from string import ascii_lowercase
        
        MCTable = [".-","-...","-.-.","-..",".","..-.","--.","....",
                   "..",".---","-.-",".-..","--","-.","---",".--.",
                   "--.-",".-.","...","-","..-","...-",".--","-..-",
                   "-.--","--.."]
        
        MCTranslate = {}
        
        transformations = set()
        
        for number in range(26):
            
            MCTranslate[ascii_lowercase[number]] = MCTable[number]
            
        for word in words:
            
            transformations.add("".join([MCTranslate[letter] for letter in word]))
                            
        return len(transformations)
