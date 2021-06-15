# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
# DONE

class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def find_father(visited, v1, v2):
    for v in visited:
        if v.info >= v1 and v.info <= v2:
            return v

def lca(root, v1, v2):
    level = []
    level.append(root)
    visited = []
    v1_, v2_ = v1, v2
    v1 = min(v1_, v2_)
    v2 = max(v1_, v2_)

    while len(level) > 0:
        node = level.pop(0)
        visited.append(node)
        if node.left is not None:
            if node.left.info == v1 or node.left.info == v2:
                visited.append(node.left)
                return find_father(visited, v1, v2)
            level.append(node.left)
            
        if node.right is not None:
            if node.right.info == v1 or node.right.info == v2:
                visited.append(node.right)
                return find_father(visited, v1, v2)
            level.append(node.right)


tree = BinarySearchTree()