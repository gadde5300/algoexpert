# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    sums = []
    helper(root,sums,0)
    return sums

def helper(cur,array,cost):
    if cur is None:
        return
    cost += cur.value
    # check.append(cur.value)
    if cur.left is None and cur.right is None:
        array.append(cost)
        return
    helper(cur.left,array,cost)
    helper(cur.right,array,cost)