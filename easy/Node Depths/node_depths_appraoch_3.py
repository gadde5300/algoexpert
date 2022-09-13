def nodeDepths(root,level=0):
    sums = 0
    def helper(node,depth):
        nonlocal sums
        if node==None:
            return
    
        sums += depth
        # print(sums,depth,node.value)
        helper(node.left,depth+1)
        helper(node.right,depth+1)

    helper(root,0)
    return sums
        
    
    


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
