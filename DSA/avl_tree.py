import sys

# Create a tree node
class TreeNode(object):
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    # get height of the node
    def getHeight(self,root):
        if not root:
            return 0
        return root.height

    # getBalance factor of Node
    def getBalance(self,root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def getMinValueNode(self,root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def rightRotate(self,node):
        leftNode = node.left
        rightNode = leftNode.right
        leftNode.right = node
        node.left = rightNode
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        leftNode.height = 1 + max(self.getHeight(leftNode.left),self.getHeight(leftNode.right))
        return leftNode

    def leftRotate(self,node):
        rightNode = node.right
        leftNode = rightNode.left
        rightNode.left = node
        node.right = leftNode
        node.height = 1 + max(self.getHeight(node.left),self.getHeight(node.right))
        rightNode.height = 1 + max(self.getHeight(rightNode.left),self.getHeight(rightNode.right))
        return rightNode

    def insert_node(self,root,key):
        # find location to insert node.
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert_node(root.left,key)
        else:
            root.right = self.insert_node(root.right,key)
        root.height = 1+ max(self.getHeight(root.left),self.getHeight(root.right))

        balanceFactor = self.getBalance(root)
        if balanceFactor > 1:
            if key < root.left.key:
                return self.rightRotate(root)
            else:
                root.left=self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if key > root.right.key:
                return self.leftRotate(root)
            else:
                root.right=self.rightRotate(root.left)
                return self.leftRotate(root)
        return root

    def delete_node(self,root,key):
        # Find the node to be deleted and remove it
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete_node(root.left, key)
        elif key > root.key:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.getMinValueNode(root.right)
            root.key = temp.key
            root.right = self.delete_node(root.right,
                                          temp.key)
        if root is None:
            return root

        # Update the balance factor of nodes
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balanceFactor = self.getBalance(root)

        # Balance the tree
        if balanceFactor > 1:
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        if balanceFactor < -1:
            if self.getBalance(root.right) <= 0:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        return root

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.key), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    # Print the tree
    def printHelper(self, currPtr, indent, last):
        if currPtr != None:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "
            print(currPtr.key)
            self.printHelper(currPtr.left, indent, False)
            self.printHelper(currPtr.right, indent, True)


myTree = AVLTree()
root = None
nums = [33, 13, 52, 9, 21, 61, 8, 11]
for num in nums:
    root = myTree.insert_node(root, num)
myTree.printHelper(root, "", True)
key = 13
root = myTree.delete_node(root, key)
print("After Deletion: ")
myTree.printHelper(root, "", True)