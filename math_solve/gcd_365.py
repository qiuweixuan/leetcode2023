#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 15:51
@Author  : dragonwxqiu
@File    ：gcd_365.py
@Software: PyCharm
@Project ：leetcode2023
"""

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        if x + y < target:
            return False
        if x == 0 or y == 0:
            return x + y == target or target == 0

        gcd_value = self.gcd(x, y)
        return target % gcd_value == 0

    @classmethod
    def gcd(cls, x: int, y: int):
        if x < 0 or y < 0:
            return 0
        if y == 0:
            return 0
        # 保证 x>=y
        if x < y:
            y, x = x, y
        remainder = x % y
        # 辗转相除法
        while remainder > 0:
            x = y
            y = remainder
            if x < y:
                y, x = x, y
            remainder = x % y
        return y
