from typing import List


class Solution:
    def __init__(self):
        self.tmp_list = None

    def sort_help(self, nums: List[int], left, right):
        # 只有一个元素或者没有元素
        if left >= right:
            return
        # middle_value = nums[left]
        """
        三数取中，实际上使用冒泡算法
        """
        mid = (left + right) // 2
        self.sort_help(nums, left, mid)
        self.sort_help(nums, mid + 1, right)
        x = left
        y = mid + 1
        # 合并两个数组
        idx = 0
        while x <= mid and y <= right:
            if nums[x] <= nums[y]:
                self.tmp_list[idx] = nums[x]
                x = x + 1
                idx = idx + 1
            else:
                self.tmp_list[idx] = nums[y]
                y = y + 1
                idx = idx + 1

        while x <= mid:
            self.tmp_list[idx] = nums[x]
            x = x + 1
            idx = idx + 1
        while y <= right:
            self.tmp_list[idx] = nums[y]
            y = y + 1
            idx = idx + 1
        #   回填数据
        for idx in range(0, right - left + 1):
            nums[left + idx] = self.tmp_list[idx]

    def sortArray(self, nums: List[int]) -> List[int]:
        self.tmp_list = [0]* len(nums)

        self.sort_help(nums, 0, len(nums) - 1)
        return nums
