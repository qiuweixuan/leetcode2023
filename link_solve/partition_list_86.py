#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/15 16:01
@Author  : dragonwxqiu
@File    ：partition_list_86.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional
from link_solve.list_node_class import ListNode


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = None
        right_head = None
        if head is None:
            return head
        # 移动指针
        cur_ptr: Optional[ListNode] = head
        left_ptr: Optional[ListNode] = None
        right_ptr: Optional[ListNode] = None
        while cur_ptr is not None:
            # 提前获取下一个元素，入栈
            next_ptr = cur_ptr.next
            # 提前把当前元素的下一个指针置为空
            cur_ptr.next = None
            # 判断移入哪个区间的链表
            if cur_ptr.val < x:
                left_head, left_ptr = self.insert_elem(left_head, left_ptr, cur_ptr)
            else:
                right_head, right_ptr = self.insert_elem(right_head, right_ptr, cur_ptr)
            cur_ptr = next_ptr
        # 拼接两个链表
        if left_head is None:
            return right_head
        elif right_head is None:
            return left_head
        else:
            left_ptr.next = right_head
            return left_head

    def insert_elem(self, move_head: Optional[ListNode], move_ptr: Optional[ListNode], cur_ptr: Optional[ListNode]) -> \
            tuple[Optional[ListNode], Optional[ListNode]]:
        if move_head is None:
            # 头插入元素
            move_head = cur_ptr
            move_ptr = cur_ptr
        else:
            # 尾插入元素
            move_ptr.next = cur_ptr
            move_ptr = cur_ptr
        return move_head, move_ptr
