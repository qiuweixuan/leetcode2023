from typing import List


class Solution:
    def __init__(self):
        self.k_min = None

    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.k_min = len(nums) - k
        return self.k_min_help(nums, 0, len(nums) - 1)

    def k_min_help(self, nums: List[int], left: int, right: int):
        # 双指针法，收敛到一个位置，则为k_min位置（递归终止条件）
        if left == right:
            return nums[left]
        # pivot = nums[left]
        mid = (left + right) // 2
        # 左中比（保证左小于中）
        if nums[left] > nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        # 右中比（保证右大于中，这样右边就是最大的元素）
        if nums[mid] > nums[right]:
            nums[mid], nums[right] = nums[right], nums[mid]
        # 左中比（左小于中，这样中就是中数）
        if nums[left] > nums[mid]:
            nums[left], nums[mid] = nums[mid], nums[left]
        pivot = nums[mid]
        x = left
        y = right
        while x <= y:
            while x <= y and nums[x] < pivot:
                x = x + 1
            while x <= y and nums[y] > pivot:
                y = y - 1
            if x <= y:
                nums[x], nums[y] = nums[y], nums[x]
                x = x + 1
                y = y - 1
        #  小于在左区间查找
        if self.k_min < x:
            return self.k_min_help(nums, left, x - 1)
        # 大于等于在右区间查找（记得等于不能退出，因为右半边还未排序）
        else:
            return self.k_min_help(nums, x, right)

