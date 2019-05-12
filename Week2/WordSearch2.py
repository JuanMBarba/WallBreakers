from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def get_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if index not in root.children:
                root.children[index] = self.get_node()
            root = root.children.get(index)

        root.terminating = True

    def search(self, word):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)

        return True if root and root.terminating else False
    
    def prefix(self, word):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])
            if not root:
                return False
            root = root.children.get(index)

        return True if root else False

    def delete(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = self.get_index(word[i])

            if not root:
                print ("Word not found")
                return -1
            root = root.children.get(index)

        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        lenr = len(board)
        lenc = len(board[0])
        result = set()
        maxDepth = 0
        leastDepth = 100000000
        def checkWord(fullWord, usedCells, curIndex):
            
            
            usedCells.add(curIndex)
            
            
            if len(fullWord) > maxDepth or not trie.prefix(fullWord):
                return
            
            if len(fullWord) >= leastDepth and trie.search(fullWord):
                result.add(fullWord)
            
            
            'Up'
            if curIndex[0] - 1 != -1 and (curIndex[0]-1, curIndex[1]) not in usedCells:
                checkWord(fullWord+board[curIndex[0]-1][curIndex[1]],set(usedCells), (curIndex[0]-1,curIndex[1]) )
            "down"
            if curIndex[0] + 1 < lenr and (curIndex[0]+1, curIndex[1]) not in usedCells:
                checkWord(fullWord+board[curIndex[0]+1][curIndex[1]],set(usedCells), (curIndex[0]+1,curIndex[1]))
            'left'
            if curIndex[1] - 1 != -1 and (curIndex[0], curIndex[1]-1) not in usedCells:
                checkWord(fullWord+board[curIndex[0]][curIndex[1]-1],set(usedCells), (curIndex[0],curIndex[1]-1) )
            "right"
            if curIndex[1] + 1 < lenc and (curIndex[0], curIndex[1]+1) not in usedCells:
                checkWord(fullWord+board[curIndex[0]][curIndex[1]+1],set(usedCells), (curIndex[0],curIndex[1]+1) )
        
        for word in words:
            trie.insert(word)
            if len(word)> maxDepth:
                maxDepth = len(word)
            if len(word) < leastDepth:
                leastDepth = len(word)
        for irow in range(lenr):
            for icol in range(lenc):
                if trie.prefix(board[irow][icol]):
                    checkWord(board[irow][icol], set(), (irow,icol))
                
        
        return list(result)
