# Binary Tree in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
        if self.right:
            self.right.traversePostOrder()
        print(self.val, end=' ')

## check full binary tree i.e each node have either both node or none
def isFullTree(root):

    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (isFullTree(root.left) and isFullTree(root.right))

    return False

### check if tree is perfect Binary Tree
#"""A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the
# leaf nodes are at the same level."""
# Calculate the depth
def calculateDepth(node):
    d = 0
    while (node is not None):
        d += 1
        node = node.left
    return d

# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):

    # Check if the tree is empty
    if (root is None):
        return True

    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)

    if (root.left is None or root.right is None):
        return False

    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)

print("Pre order Traversal: ", end="")
root.traversePreOrder()
print("\nIn order Traversal: ", end="")
root.traverseInOrder()
print("\nPost order Traversal: ", end="")
root.traversePostOrder()

print ("\n The tree is full Binary Tree? %s" % isFullTree(root),end="")
print ("\n The tree is Perfect Binary Tree? %s" %is_perfect(root,calculateDepth(root)))

root = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

if (is_perfect(root, calculateDepth(root))):
    print("The tree2 is a perfect binary tree")
else:
    print("The tree2 is not a perfect binary tree")





# #A complete binary tree is just like a full binary tree, but with two major differences
# #All the leaf elements must lean towards the left.
# #The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
# # Count the number of nodes
# # This function counts the number of nodes in a binary tree
# def countNodes(root):
#     if root is None:
#         return 0
#     return (1 + countNodes(root.leftChild) + countNodes(root.rightChild))
#
# # This function checks if binary tree is complete or not
# def isComplete(root, index, number_nodes):
#     # An empty is complete
#     if root is None:
#         return True
#
#     # If index assigned to current nodes is more than
#     # number of nodes in tree, then tree is not complete
#     if index >= number_nodes:
#         return False
#
#     # Recur for left and right subtress
#     return (isComplete(root.leftChild, 2 * index + 1, number_nodes)
#             and isComplete(root.rightChild, 2 * index + 2, number_nodes))
#
#
# # Driver Program
#
# root = Node(1)
# root.leftChild = Node(2)
# root.rightChild = Node(3)
# root.leftChild.leftChild = Node(4)
# root.leftChild.rightChild = Node(5)
# node_count = countNodes(root)
# index = 0
#
# if isComplete(root, index, node_count):
#     print("The Binary Tree is complete")
# else:
#     print("The Binary Tree is not complete")
#
# root = Node(1)
# root.leftChild = Node(2)
# root.rightChild = Node(3)
# root.leftChild.leftChild = Node(4)
# root.leftChild.rightChild = Node(5)
# root.rightChild.leftChild = Node(6)
# root.rightChild.leftChild = Node(7)
#
# node_count = countNodes(root)
# index = 0
#
# if isComplete(root, index, node_count):
#     print("The Binary Tree is complete")
# else:
#     print("The Binary Tree is not complete")

def countNodes(root):
    if root is None:
        return 0
    return (1 + countNodes(root.left) + countNodes(root.right))


# This function checks if binary tree is complete or not
def isComplete(root, index, number_nodes):
    # An empty is complete
    if root is None:
        return True

    # If index assigned to current nodes is more than
    # number of nodes in tree, then tree is not complete
    if index >= number_nodes:
        return False

    # Recur for left and right subtress
    return (isComplete(root.left, 2 * index + 1, number_nodes)
            and isComplete(root.right, 2 * index + 2, number_nodes)
            )


# Driver Program

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

node_count = countNodes(root)
index = 0

if isComplete(root, index, node_count):
    print("The Binary Tree is complete")
else:
    print("The Binary Tree is not complete")