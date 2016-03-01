# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree_recur(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        递归解法(DFS)
        """
        if not root:
            return root

        (root.left, root.right) = (self.invertTree_recur(root.right),
                                   self.invertTree_recur(root.left))
        return root

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Iterative solution(BFS)
        """

        if not root:
            return root

        queue = []
        result = []
        cur = None

        queue.append(root)
        while queue:
            cur = queue.pop(0)
            result.append(cur)

            if cur.right:
                queue.append(cur.right)

            if cur.left:
                queue.append(cur.left)

        while result:
            cur = result.pop()
            cur.left, cur.right = cur.right, cur.left

        return cur

