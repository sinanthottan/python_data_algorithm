class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        global max_level
        max_level = [0]

    #add child
    def add_child(self,data):
        if self.data == data:
            return

        if data < self.data:
            #left node
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            #right node
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def inorder_traversal(self):
        elements = []

        #visit left
        if self.left:
            elements += self.left.inorder_traversal()

        #visit base node
        elements.append(self.data)

        #visit right Node
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self,val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def left_view(self, max_level, level):
        #base case
        if self.data:
            #check if it is first node of its level
            if max_level[0] < level:
                print(self.data)
                max_level[0] = level
            #recurring through left node
            if self.left : self.left.left_view(max_level,level+1)
            #recurring through right node
            if self.right : self.right.left_view(max_level,level+1)



def build_tree(data):
    root = BinarySearchTreeNode(data[0])
    for i in range(1,len(data)):
        root.add_child(data[i])

    return root


numbers = [9,10,11,13,12,15,4,6,3,5]
tree = build_tree(numbers)
#print(tree.inorder_traversal())
tree.left_view(max_level,1)
