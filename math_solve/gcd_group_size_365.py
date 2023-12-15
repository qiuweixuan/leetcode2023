#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/14 16:51
@Author  : dragonwxqiu
@File    ：gcd_group_size_365.py
@Software: PyCharm
@Project ：leetcode2023
"""
import math
from typing import List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        """
        使用字典来保存长度
        :param deck:
        :return:
        """
        deck_size_dict = {}
        for value in deck:
            value_size = deck_size_dict.get(value, 0)
            deck_size_dict[value] = value_size + 1
        # 排序
        deck_size_list = list(deck_size_dict.values())
        deck_size_list.sort()
        if len(deck_size_list) == 1:
            return deck_size_list[0] >= 2

        # 初始计算remainder
        remainder = math.gcd(deck_size_list[0], deck_size_list[1])
        for elem in deck_size_list[2:]:
            remainder = math.gcd(remainder, elem)
        return remainder >= 2