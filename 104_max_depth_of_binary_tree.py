# -*- coding: utf-8 -*-

#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        if self.is_leaf(root):
            return 1

        if root.left:
            left_depth = self.maxDepth(root.left)
        else:
            left_depth = 0

        if root.right:
            right_depth = self.maxDepth(root.right)
        else:
            right_depth = 0

        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def is_leaf(self, node):
        """docstring for is_root"""
        return (not node.left and not node.right)

class SolutionPythonic(object):
    #more pythonic
    def maxDepth(self, root):
        return self.fathom(root, 0)

    def fathom(self, root, depth):
        if not root: return depth
        else: return max(self.fathom(root.left, depth+1), self.fathom(root.right, depth+1))
