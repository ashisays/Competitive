class Node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val

class Tree:
    def __init__(self,val):
        self.root = Node(val)

    # A utility function to insert a new node with the given val
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

    def search(self,root, val):
        # Base Cases: root is null or val is present at root
        if root is None or root.val == val:
            return root
            # val is greater than root's val
        if root.val < val:
            return self.search(root.right, val)
            # val is smaller than root's val
        return self.search(root.left, val)

    def deleteNode(self,root, val):
        # Base Case
        if root is None:
            return root
        # If the val to be deleted is smaller than the root's
        # val then it lies in  left subtree
        if val < root.val:
            root.left = self.deleteNode(root.left,val)

        # If the kye to be delete is greater than the root's val
        # then it lies in right subtree
        elif val > root.val:
            root.rigth = self.deleteNode(root.right,val)
        # If val is same as root's val, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.minValueNode(root.right)
            # Copy the inorder successor's content to this node
            root.val = temp.val
            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)
        return root

        # Driver program to test above functions
""" Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 """

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

# print("\nDelete 20")
# root = t.deleteNode(t.root, 20)
# print("Inorder traversal of the modified tree")
# t.inorder(t.root)
#
# print("\nDelete 30")
# root = t.deleteNode(t.root, 30)
# print("Inorder traversal of the modified tree")
# t.inorder(t.root)
# print("\nDelete 50")
# root = t.deleteNode(t.root, 70)
# print("Inorder traversal of the modified tree")
# t.inorder(t.root)


print("\nDelete ")
root = t.deleteNode(t.root, 40)
print("Inorder traversal of the modified tree")
t.inorder(t.root)