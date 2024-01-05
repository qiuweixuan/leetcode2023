#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/4 14:36
@Author  : dragonwxqiu
@File    ：longest_sub_palindrome_516.py
@Software: PyCharm
@Project ：leetcode2023
"""


class Solution:
    """
    dp问题：
    1. 基准值dp[i][i] = 1,dp[i][j] = 0
    2. 转移方程：
        if s[i] == s[j]: dp[i][j] = dp[i+1][j-1] + 2
        else: dp[i][j] = max(dp[i+1][j],dp[i,j-1]
        需要i倒序,j正序遍历
    3. 最终结果： dp[0][n-1]
    """

    def longestPalindromeSubseq(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0
        # 基准值初始化
        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1
        # 推进dp转移,也是左右端点的思想
        for i in reversed(range(size)):
            for j in range(size):
                if i >= j:
                    continue

                if s[i] == s[j]:
                    if i + 1 <= j - 1:
                        sub_value = dp[i + 1][j - 1]
                    else:
                        sub_value = 0
                    dp[i][j] = sub_value + 2
                else:
                    if 0 <= j - 1 < size:
                        sub_value_left = dp[i][j - 1]
                    else:
                        sub_value_left = 0
                    if 0 <= i + 1 < size:
                        sub_value_right = dp[i + 1][j]
                    else:
                        sub_value_right = 0
                    dp[i][j] = max(sub_value_left, sub_value_right)
        return dp[0][size - 1]
