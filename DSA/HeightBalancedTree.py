# Checking if a binary tree is CalculateHeight balanced in Python
# CreateNode creation
#difference between the left and the right subtree for any node is not more than one
#the left subtree is balanced
#the right subtree is balanced
class CreateNode:

    def __init__(self, item):
        self.item = item
        self.left = self.right = None

# Calculate height
class CalculateHeight:
    def __init__(self):
        self.CalculateHeight = 0

# Check height balance
def is_height_balanced(root, Height):
    left_height = CalculateHeight()
    right_height = CalculateHeight()

    if root is None:
        return True

    l = is_height_balanced(root.left, left_height)
    r = is_height_balanced(root.right, right_height)

    Height.CalculateHeight = max(
        left_height.CalculateHeight, right_height.CalculateHeight) + 1
    if abs(left_height.CalculateHeight - right_height.CalculateHeight) <= 1:
        return l and r
    return False

root = CreateNode(1)
root.left = CreateNode(2)
root.right = CreateNode(3)
root.left.left = CreateNode(4)
root.left.right = CreateNode(5)
root.right.right = CreateNode(6)
root.right.right.left = CreateNode(7)

if is_height_balanced(root, CalculateHeight()):
     print('The tree is balanced')
else:
     print('The tree is not balanced')