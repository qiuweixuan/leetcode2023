#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2023/12/20 15:11
@Author  : dragonwxqiu
@File    ：longest_palindrome.py
@Software: PyCharm
@Project ：leetcode2023
"""


class Solution:

    def longestPalindrome(self, s: str) -> str:
        """
        回文串自底向上解法
        1. 回文串首尾一定是相等字符
        2. 回文串内部一定是回文串
        实际上符合贪心算法的本质
        :param s:
        :return:
        """
        # 二维数组构建
        size = len(s)
        is_palind_dp = [[None for _ in range(size)] for _ in range(size)]

        max_size = 0
        max_left = -1
        max_right = -1
        for step in range(size):
            for left in range(size - step):
                right = left + step
                # 基准条件
                if step + 1 == 1:
                    is_palind_dp[left][right] = True
                elif step + 1 == 2:
                    is_palind_dp[left][right] = (s[left] == s[right])
                # 扩展条件
                else:
                    is_palind_dp[left][right] = (s[left] == s[right]) and is_palind_dp[left + 1][right - 1]

                if is_palind_dp[left][right]:
                    max_size = right - left + 1
                    max_left = left
                    max_right = right
            if step + 1 >= max_size + 2:
                break
        return s[max_left:max_right + 1]

    def longestPalindromeV2(self, s: str) -> str:
        size = len(s)
        max_size = 0
        max_res = ''
        for i in range(size):
            one_middle_str = self.helper(s, i, i)
            if i + 1 < size:
                two_middle_str = self.helper(s, i, i + 1)
            else:
                two_middle_str = None
            if one_middle_str is not None and len(one_middle_str) > max_size:
                max_size = len(one_middle_str)
                max_res = one_middle_str
            if two_middle_str is not None and len(two_middle_str) > max_size:
                max_size = len(two_middle_str)
                max_res = two_middle_str
        return max_res


    def helper(self, s: str, left: int, right: int) -> str:
        size = len(s)
        while left >= 0 and right < size and s[left] == s[right]:
            left = left - 1
            right = right + 1
        left = left + 1
        right = right - 1
        if s[left] == s[right]:
            return s[left:right + 1]
        else:
            return None
