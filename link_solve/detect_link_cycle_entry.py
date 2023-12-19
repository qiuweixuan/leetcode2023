#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/18 19:44
@Author  : dragonwxqiu
@File    ：detect_link_cycle_entry.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional

from link_solve.list_node_class import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        slow = head
        fast = head
        #  查找相交节点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        # 如果不符合条件就不是环
        if fast is None or fast.next:
            return None
        head_ptr = head
        while head_ptr != slow:
            head_ptr = head_ptr.next
            slow = slow.next
        return slow

