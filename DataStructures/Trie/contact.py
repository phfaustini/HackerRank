# https://www.hackerrank.com/challenges/contacts

class Trie():
    def __init__(self, c):
        self.char = c
        self.children = []
        
    def getChar(self):
        return self.char
    
    def addChild(self, node):
        self.children.append(node)
        
    
def add(word):
    pass

def find(subword):
    pass

if __name__ == "__main__":
    operations = int(input())
    while operations > 0:
        operations -= 1
        line = input().split()
        if line[0][0] == 'a': #add
            add(line[1])
        else: # find
            print (find(line[1]))
        