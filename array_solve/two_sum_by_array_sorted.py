#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 14:21
@Author  : dragonwxqiu
@File    ：two_sum_by_array_sorted.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """

        :param numbers:
        :param target:
        :return:
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur_sum = numbers[left] + numbers[right]
            # 求解答案
            if cur_sum == target:
                return [left + 1, right + 1]
            # 无解答案
            if left + 1 == right:
                return [-1, -1]
            # 左指针太小
            if cur_sum < target:
                left = left + 1
            else:
                right = right - 1
        return [-1, -1]