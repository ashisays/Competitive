class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

class Tree:
    def __init__(self,key):
        self.root = Node(key)

    # A utility function to insert a new node with the given key
    @classmethod
    def insert(self,root,node):
        if root is None:
            root = node
        else:
            if root.val < node.val:
                if root.right is None:
                    root.right = node
                else:
                    self.insert(root.right, node)
            else:
                if root.left is None:
                    root.left = node
                else:
                    self.insert(root.left, node)

    # A utility function to do inorder tree traversal
    @classmethod
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)

    def minValueNode(self,node=None):
        if node == None:
            node = self.root
        current = node
        # loop down to find the leftmost leaf
        while (current.left is not None):
            current = current.left
        return current

    def search(self,root, key):
        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return root
            # Key is greater than root's key
        if root.val < key:
            return self.search(root.right, key)
            # Key is smaller than root's key
        return self.search(root.left, key)

    

t = Tree(50)
t.insert(t.root,Node(30))
t.insert(t.root,Node(20))
t.insert(t.root,Node(40))
t.insert(t.root,Node(70))
t.insert(t.root,Node(60))
t.insert(t.root,Node(80))

t.inorder(t.root)
print("MIn Value of Node : %s" %t.minValueNode().val)
print("Searchin the node value 30 : %s" %t.search(t.root,30).val)