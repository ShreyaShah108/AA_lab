import math

points = [[6, 2], [7, 1], [2, 9], [3, 6], [4, 8], [8, 4], [5, 3], [1, 5], [9, 5]]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class KDtree:
    def __init__(self):
        self.root = None

    def sortData(self,data,index):
        for i in range(len(data)):
            for j in range(i+1,len(data)):
                if data[i][index]>data[j][index]:
                    data[i],data[j] = data[j],data[i]
        return data

    def getMiddle(self,data):
        index = math.ceil(len(data)/2)-1
        return index

    def create(self,data,index,par,flag):
        if data != []:
            print("Data: ",data)
            result = self.sortData(data,index)
            middle = self.getMiddle(result)
            print("Sorted Data: ",result)
            print(f"Middle Element: {result[middle]} \n")
            nn = Node(result[middle])
            if self.root is None:
                self.root = nn
            else:
                if flag == 0:
                    par.left = nn
                else:
                    par.right = nn
            self.create(result[0:middle],(index+1)%2,nn,0)
            self.create(result[middle+1:],(index+1)%2,nn,1)
    
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)
        

instance = KDtree()
instance.create(points,0,None,0)
instance.inorder_traversal(instance.root)