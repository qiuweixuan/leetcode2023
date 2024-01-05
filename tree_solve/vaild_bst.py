#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 17:01
@Author  : dragonwxqiu
@File    ：vaild_bst.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from tree_solve.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.prev: Optional[TreeNode] = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev = None
        return self.in_order_reverse(root)

    def in_order_reverse(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        is_left_bst = self.in_order_reverse(root.left)
        is_bst = True
        if self.prev is not None:
            is_bst = self.prev.val < root.val
        self.prev = root
        is_right_bst = self.in_order_reverse(root.right)
        return is_left_bst and is_bst and is_right_bst
