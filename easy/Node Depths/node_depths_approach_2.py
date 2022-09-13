def nodeDepths(root):
	depth_sum = 0
	stack = [{"node":root,"depth": 0}]
	
	while len(stack) > 0:
		nodeinfo = stack.pop()
		node,depth = nodeinfo["node"],nodeinfo["depth"]
		if node is None: 
			continue
		depth_sum += depth
		stack.append({"node":node.left,"depth":depth+1})
		stack.append({"node":node.right,"depth":depth+1})
	return depth_sum


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
