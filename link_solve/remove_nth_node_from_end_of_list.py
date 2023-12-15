#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 19:26
@Author  : dragonwxqiu
@File    ：remove_nth_node_from_end_of_list.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional
from link_solve.list_node_class import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow_ptr = head
        fast_ptr = head
        # 移动快指针
        for _ in range(n):
            if fast_ptr is not None:
                fast_ptr = fast_ptr.next
            else:
                return head
        #  说明需要删头节点
        if fast_ptr is None:
            ret_ptr = slow_ptr.next
            slow_ptr.next = None
            # 相当于return head.next
            return ret_ptr
        # 剩下的都是要删除中间节点
        while fast_ptr is not None:
            # 先移动快指针，再判断
            fast_ptr = fast_ptr.next
            if fast_ptr is None:
                del_ptr = slow_ptr.next
                slow_ptr.next = slow_ptr.next.next
                del_ptr.next = None
                return head
            # 不需要删除，则移动慢指针
            slow_ptr = slow_ptr.next