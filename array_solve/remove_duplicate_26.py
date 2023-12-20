#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 09:57
@Author  : dragonwxqiu
@File    ：remove_duplicate_26.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        result_list = []
        before_value = None
        for cur_value in nums:
            if cur_value != before_value:
                result_list.append(cur_value)
                before_value = cur_value

        result_size = len(result_list)
        for i in range(result_size):
            nums[i] = result_list[i]
        return result_size

    def removeDuplicatesNav(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        slow_index = 0
        for cur_value in nums:
            if cur_value != nums[slow_index]:
                nums[slow_index + 1] = cur_value
                slow_index = slow_index + 1
        return slow_index + 1
