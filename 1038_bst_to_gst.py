# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        nodes = []
        def preprocess(node: TreeNode):
            if node.right:
                preprocess(node.right)

            nodes.append(node)

            if node.left:
                preprocess(node.left)

        preprocess(root)
        nodes.reverse()

        while len(nodes) > 0:
            node = nodes.pop()

        

if __name__ == '__main__':
    vals = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    vals.reverse()
    root = TreeNode(vals.pop())
    nodes = [root]
    while len(vals) > 0:
        last_node = nodes.pop()
        left_node = TreeNode(vals.pop())
        right_node = TreeNode(vals.pop())
        last_node.left = left_node
        last_node.right = right_node
        if left_node.val is not None:
            nodes.insert(0, left_node)
        if left_node.val is not None:
            nodes.insert(0, right_node)

    # results = []

    # unvisited = [root]
    # while len(unvisited) > 0:
    #     node = unvisited.pop()
    #     results.append(node.val)

    #     if node.left:
    #         unvisited.insert(0, node.left)
    #     if node.right:
    #         unvisited.insert(0, node.right)
    s = Solution()
    result = s.bstToGst(root)
    print(result)