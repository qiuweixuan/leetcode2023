#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/18 19:18
@Author  : dragonwxqiu
@File    ：middle_of_list.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from link_solve.list_node_class import ListNode


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        size = 0
        slow = head
        fast = head
        while fast is not None:
            fast = fast.next
            size = size + 1
        slow_move = int(size / 2) + 1 - 1
        for i in range(slow_move):
            slow = slow.next
        return slow

    def middleNodeV2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        slow = head
        fast = head
        # 向下取整算法
        while fast and fast.next:
            # 利用空间局部性原理
            slow = slow.next
            fast = fast.next.next
        return slow