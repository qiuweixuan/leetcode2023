#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 17:35
@Author  : dragonwxqiu
@File    ：combine_77.py
@Software: PyCharm
@Project ：leetcode2023
"""
import copy
from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.all_result = []
        self.used = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.all_result = []
        self.result = []
        self.used = [0] * (n + 1)
        self.backtrack(n, k, -1)
        return self.all_result

    def backtrack(self, n: int, k: int, before_value: int):
        if k == 0:
            self.all_result.append(copy.deepcopy(self.result))
            return

        for i in range(1, n + 1):
            if self.used[i] == 0 and i > before_value:
                self.used[i] = 1
                self.result.append(i)
                self.backtrack(n, k - 1, i)
                self.result.pop()
                self.used[i] = 0


class Solution2:
    def __init__(self):
        self.result = []
        self.all_result = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        self.all_result = []
        self.result = []
        self.backtrack(n, k, 0)
        return self.all_result

    def backtrack(self, n: int, k: int, before_value: int):
        if k == 0:
            self.all_result.append(copy.deepcopy(self.result))
            return
        if before_value + k > n:
            return
        for i in range(before_value + 1, n + 1):
            self.result.append(i)
            self.backtrack(n, k - 1, i)
            self.result.pop()

