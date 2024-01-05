#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 17:17
@Author  : dragonwxqiu
@File    ：kth_bst.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from tree_solve.tree_node import TreeNode


class Solution:
    def __init__(self):
        self.result = -1
        self.cnt = None

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.cnt = 0
        self.result = -1
        self.kth = k
        self.in_order_reverse(root)
        return self.result

    def in_order_reverse(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.in_order_reverse(root.left)
        self.cnt += 1
        if self.cnt == self.kth:
            self.result = root.val
        self.in_order_reverse(root.right)
