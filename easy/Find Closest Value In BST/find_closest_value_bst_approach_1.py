def findClosestValueInBst(tree, target):
    return helper(tree,target,float('inf'))

def helper(tree,target,check):
    if not tree:
        return check
    if abs(target-check) > abs(target-tree.value):
        check = tree.value
    if target > tree.value:
        return helper(tree.right,target,check)
    elif target < tree.value:
        return helper(tree.left,target,check)
    elif target == tree.value:
        return target


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
