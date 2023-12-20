#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 11:21
@Author  : dragonwxqiu
@File    ：remove_duplicate_83.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from link_solve.list_node_class import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow_ptr = head
        fast_ptr = head
        while fast_ptr is not None:
            if fast_ptr.val != slow_ptr.val:
                slow_ptr.next = fast_ptr
                slow_ptr = fast_ptr
            fast_ptr = fast_ptr.next
        slow_ptr.next = None
        return dummy.next