#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 17:37
@Author  : dragonwxqiu
@File    ：intersection-of-two-linked-lists.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional
from link_solve.list_node_class import ListNode


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
        cur_head_a = head_a
        cur_head_b = head_b

        head_a_size = 0
        while cur_head_a is not None:
            head_a_size += 1
            cur_head_a = cur_head_a.next

        head_b_size = 0
        while cur_head_b is not None:
            head_b_size += 1
            cur_head_b = cur_head_b.next

        cur_head_a = head_a
        cur_head_b = head_b
        if head_b_size > head_a_size:
            for _ in range(head_b_size - head_a_size):
                cur_head_b = cur_head_b.next
        elif head_b_size < head_a_size:
            for _ in range(head_a_size - head_b_size):
                cur_head_a = cur_head_a.next

        while cur_head_a is not None or cur_head_b is not None:
            if cur_head_a == cur_head_b:
                return cur_head_b
            cur_head_a = cur_head_a.next
            cur_head_b = cur_head_b.next
        return None
