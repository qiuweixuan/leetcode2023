from typing import List


class Solution:
    def sort_help(self, nums: List[int], left, right):
        # 只有一个元素或者没有元素
        if left >= right:
            return
        # middle_value = nums[left]
        """
        三数取中，实际上使用冒泡算法
        """
        mid = (left + right) // 2
        # 左中比（保证左小于中）
        if nums[left] > nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        # 右中比（保证右大于中，这样右边就是最大的元素）
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        # 左中比（左大于中，这样取左就是中数）
        if nums[left] <= nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]

        # 左右指针，左闭右闭法
        x = left
        y = right
        middle_value = nums[x]
        # 不断调整中间边界，x <= y 防止越界
        while x < y:
            while x < y and nums[y] >= middle_value:
                y = y - 1
            nums[x] = nums[y]
            # 查找无序元素（左找大于等于，右找小于等于）
            while x < y and nums[x] <= middle_value:
                x = x + 1
            nums[y] = nums[x]
        nums[x] = middle_value
        """
        边界处理,应用不变式思想
        """
        # x和y之间是middle_value取值区间
        #  不变式1: nums[y] <=  middle_value
        self.sort_help(nums, left, x - 1)
        #  不变式2: nums[x] >=  middle_value
        self.sort_help(nums, x + 1, right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.sort_help(nums, 0, len(nums) - 1)
        return nums
