#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 11:36
@Author  : dragonwxqiu
@File    ：remove_elem.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        before_size = len(nums)
        remove_size = 0
        slow_index = 0
        fast_index = 0
        # 使用None表示空值
        while slow_index < before_size:
            # 先找到一个需要删除的值下标
            # 找到对应值 或者 找到空值 => 就停下来
            while slow_index < before_size and nums[slow_index] != val and nums[slow_index] is not None:
                slow_index += 1
            # 找到需要删除的元素
            if slow_index < before_size and nums[slow_index] == val :
                remove_size += 1
            # 快指针从慢指针的右边找一个元素填充
            fast_index = max(fast_index, slow_index + 1)
            while fast_index < before_size and (nums[fast_index] == val or nums[fast_index] is None):
                fast_index += 1
            #  开始用后一个元素替换前一个元素
            if fast_index < before_size:
                nums[slow_index] = nums[fast_index]
                nums[fast_index] = None
            # 移动各自指针
            slow_index += 1
        after_size = before_size - remove_size
        return after_size
