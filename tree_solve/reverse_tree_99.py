#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 16:36
@Author  : dragonwxqiu
@File    ：reverse_tree_99.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from tree_solve.tree_node import TreeNode


class Solution:
    """
    使用中序遍历递增原理
    """

    def __init__(self):
        self.first: Optional[TreeNode] = None
        self.second: Optional[TreeNode] = None
        self.prev: Optional[TreeNode] = None

    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = None
        self.in_order_traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def in_order_traverse(self, root: Optional[TreeNode]):
        """
        中序遍历
        :param root:
        :return:
        """
        if root is None:
            return
        self.in_order_traverse(root.left)
        if self.prev is not None and self.prev.val > root.val:
            if self.first is None:
                self.first = self.prev
            self.second = root
        self.prev = root
        self.in_order_traverse(root.right)
