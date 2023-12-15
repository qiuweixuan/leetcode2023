#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 17:19
@Author  : dragonwxqiu
@File    ：linked_list_cycle_141.py
@Software: PyCharm
@Project ：leetcode2023
"""


from typing import Optional
from link_solve.list_node_class import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_ptr = head
        slow_ptr = head
        while fast_ptr is not None:
            # 快指针
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return False
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                return False
            # 慢指针
            slow_ptr = slow_ptr.next
            if fast_ptr == slow_ptr:
                return True
        return False