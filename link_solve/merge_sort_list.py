#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 19:49
@Author  : dragonwxqiu
@File    ：merge_sort_list.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import Optional, List
import heapq

from link_solve.list_node_class import ListNode


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # 都不是非空列表
        list1_ptr = list1
        list2_ptr = list2
        if list1_ptr.val <= list2_ptr.val:
            head = list1_ptr
            list1_ptr = list1_ptr.next
        else:
            head = list2_ptr
            list2_ptr = list2_ptr.next
        # 双边推进
        cur_ptr = head
        while list1_ptr is not None and list2_ptr is not None:
            if list1_ptr.val <= list2_ptr.val:
                cur_ptr.next = list1_ptr
                list1_ptr = list1_ptr.next
            else:
                cur_ptr.next = list2_ptr
                list2_ptr = list2_ptr.next
            cur_ptr = cur_ptr.next

        # 处理单边情况
        if list1_ptr is None:
            cur_ptr.next = list2_ptr
        if list2_ptr is None:
            cur_ptr.next = list1_ptr

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        cur_lists = lists
        next_lists = []
        while len(cur_lists) > 1:
            for i in range(0, len(cur_lists), 2):
                if i + 1 < len(cur_lists):
                    new_list = self.mergeTwoLists(cur_lists[i], cur_lists[i + 1])
                    next_lists.append(new_list)
                else:
                    new_list = cur_lists[i]
                    next_lists.append(new_list)
            cur_lists = next_lists
            next_lists = []

        if len(cur_lists) == 0:
            return None
        return cur_lists[0]

    def mergeKListsByHeap(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        1. 使用堆完成k个元素的最小值、最大值获取
        2. 使用虚拟头节点，简化链表插入操作实现
        :param lists:
        :return:
        """

        # ListNode.lt = lambda left_elem, right_elem: left_elem.val < right_elem.val
        def sort_func(left_elem: ListNode, right_elem: ListNode):
            return left_elem.val < right_elem.val

        # 自定义比较函数
        ListNode.lt = sort_func

        # 虚拟头结点
        dummy = ListNode(-1)
        # 当前指针
        cur_ptr = dummy
        # 优先级队列，最小堆
        priority_queue = []
        for head in lists:
            if head:
                # 构建（比较元素取值，元素节点）元组
                # heapq用法不是绑定到实例上，而是提供辅助函数的方式，读取数组列表中的元素
                heapq.heappush(priority_queue, (head.val, head))
        # 不断遍历优先队列，直至队列为空，说明已经遍历所有列表
        while len(priority_queue) > 0:
            _, node = heapq.heappop(priority_queue)
            cur_ptr.next = node
            cur_ptr = node
            if node.next:
                heapq.heappush(priority_queue, (node.next.val, node.next))
            cur_ptr.next = None
        # 返回头指针的下个节点
        return dummy.next