#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 15:05
@Author  : dragonwxqiu
@File    ：reverse_string.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            tmp = s[left]
            s[left] = s[right]
            s[right] = tmp
            left = left + 1
            right = right - 1
