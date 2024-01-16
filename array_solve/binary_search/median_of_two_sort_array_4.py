#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
@Time    : 2024/1/16 15:32
@Author  : dragonwxqiu
@File    ：median_of_two_sort_array_4.py
@Software: PyCharm
@Project ：leetcode2023
"""
from typing import List


class Solution:
    """
    解题思路:2分法
    1. 只移动较短数组的二分指针，另一个数组的指针由总二分数可得出（numsMid2 = allMidSize - numsMid1)
    2. 左闭右闭、左闭右开的二分查找法（模版），以及len(left_part) >= len(right_part)：
        因此需要选择靠右的中位数点位（不加1则靠左）： int((len(nums1) + len(nums2) + 1) / 2)
    3. 由2可知,奇数情况：左半部分最大(两个左半部分取大), 偶数情况：(左半部分最大 + 右半部分最小) / 2
    4. 尽量不要使用直接返回法
    """

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums1=nums2, nums2=nums1)
        # 求解点1
        low, high = 0, len(nums1)
        # 求解点2
        nums1_mid, nums2_mid, all_high_mid = 0, 0, int((len(nums1) + len(nums2) + 1) / 2)
        while low <= high:
            nums1_mid = int(low + ((high - low) / 2))
            nums2_mid = all_high_mid - nums1_mid
            # A中间指针需要左移
            if nums1_mid > 0 and nums1[nums1_mid - 1] > nums2[nums2_mid]:
                high = nums1_mid - 1
            # A中间指针需要右移
            elif nums1_mid < len(nums1) and nums2[nums2_mid - 1] > nums1[nums1_mid]:
                low = nums1_mid + 1
            else:
                break
        """
        重点！：退出循环时[low==high),此时low为中点
        """
        # nums1_mid = low
        # nums2_mid = all_high_mid - nums1_mid

        # 求左半部最大值
        if nums1_mid == 0:
            mid_left = nums2[nums2_mid - 1]
        elif nums2_mid == 0:
            mid_left = nums1[nums1_mid - 1]
        else:
            mid_left = max(nums1[nums1_mid - 1], nums2[nums2_mid - 1])

        # 奇数返回
        if (len(nums1) + len(nums2)) % 2 == 1:
            return mid_left

        # 求右半部最小值
        if nums1_mid == len(nums1):
            mid_right = nums2[nums2_mid]
        elif nums2_mid == len(nums2):
            mid_right = nums1[nums1_mid]
        else:
            mid_right = min(nums1[nums1_mid], nums2[nums2_mid])

        return (mid_left + mid_right) / 2

    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays2(nums1=nums2, nums2=nums1)
        # 求解点1
        low, high = 0, len(nums1)
        # 求解点2
        nums1_mid, nums2_mid, all_high_mid = 0, 0, int((len(nums1) + len(nums2) + 1) / 2)
        while low < high:
            nums1_mid = int(low + ((high - low) / 2))
            nums2_mid = all_high_mid - nums1_mid
            # A中间指针需要右移
            if nums1_mid < len(nums1) and nums2[nums2_mid - 1] > nums1[nums1_mid]:
                low = nums1_mid + 1
            # A中间指针需要左移
            else:
                high = nums1_mid
        """
        重点！：退出循环时[low==high),此时low为中点
        """
        nums1_mid = low
        nums2_mid = all_high_mid - nums1_mid

        """
        应该正确使用-inf和+inf数值表示
        """
        # 求左半部最大值
        if nums1_mid <= 0:
            mid_left = nums2[nums2_mid - 1]
        elif nums2_mid <= 0:
            mid_left = nums1[nums1_mid - 1]
        else:
            mid_left = max(nums1[nums1_mid - 1], nums2[nums2_mid - 1])

        # 奇数返回
        if (len(nums1) + len(nums2)) % 2 == 1:
            return mid_left

        # 求右半部最小值
        if nums1_mid >= len(nums1):
            mid_right = nums2[nums2_mid]
        elif nums2_mid >= len(nums2):
            mid_right = nums1[nums1_mid]
        else:
            mid_right = min(nums1[nums1_mid], nums2[nums2_mid])

        return (mid_left + mid_right) / 2

    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
        """
        本题是找左边界
        """
        n1 = len(nums1)
        n2 = len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays3(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        left = 0
        right = n1
        while left < right:
            m1 = left + (right - left) // 2  # 在 nums1 中取前 m1 个元素
            m2 = k - m1  # 在 nums2 中取前 m2 个元素
            if nums1[m1] < nums2[m2 - 1]:  # 说明 nums1 中所元素不够多，
                left = m1 + 1
            else:
                right = m1

        m1 = left
        m2 = k - m1

        c1 = max(float('-inf') if m1 <= 0 else nums1[m1 - 1], float('-inf') if m2 <= 0 else nums2[m2 - 1])
        if (n1 + n2) % 2 == 1:
            return c1

        c2 = min(float('inf') if m1 >= n1 else nums1[m1], float('inf') if m2 >= n2 else nums2[m2])

        return (c1 + c2) / 2
