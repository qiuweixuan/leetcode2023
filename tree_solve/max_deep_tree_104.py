#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 16:06
@Author  : dragonwxqiu
@File    ：max_deep_tree_104.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from tree_solve.tree_node import TreeNode


class Solution:
    """
    后序遍历
    """

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
