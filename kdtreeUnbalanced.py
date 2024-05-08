points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class KDtree:
    def __init__(self):
        self.root = None
    
    def create(self):
        for i in points:
            nn = Node(i)
            if self.root is None:
                self.root = nn
            else:
                depth = 0
                temp = self.root
                while temp is not None:
                    par = temp
                    if temp.data[depth%2]>i[depth%2]:
                        temp = temp.left
                    else:
                        temp = temp.right
                    depth+=1
                if par.data[(depth-1)%2]>i[(depth-1)%2]:
                    par.left = nn
                else:
                    par.right = nn
        return self.root
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

instance = KDtree()
root = instance.create()
instance.inorder_traversal(root)