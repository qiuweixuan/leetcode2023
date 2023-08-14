import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_912(self):
        from sort import quick_sort_912
        nums = [5, 2, 3, 1]
        res = quick_sort_912.Solution().sortArray(nums)
        print(res)
        nums = [5, 1, 1, 2, 0, 0]
        res = quick_sort_912.Solution().sortArray(nums)
        print(res)

    def test_912_merge(self):
        from sort.merge_sort_912 import Solution
        nums = [5, 2, 3, 1]
        res = Solution().sortArray(nums)
        print(res)
        nums = [5, 1, 1, 2, 0, 0]
        res = Solution().sortArray(nums)
        print(res)

    def test_912_pivot(self):
        from sort.quick_sort_912_pivot import Solution
        nums = [5, 2, 3, 1]
        res = Solution().sortArray(nums)
        print(res)
        nums = [5, 1, 1, 2, 0, 0]
        res = Solution().sortArray(nums)
        print(res)

    def test_215(self):
        from sort.quick_sork_k_number_215 import Solution
        nums = [3, 2, 1, 5, 6, 4]
        k = 2
        res = Solution().findKthLargest(nums, k)
        print(res)
        self.assertEqual(res, 5)
        nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
        k = 4
        res = Solution().findKthLargest(nums, k)
        print(res)
        self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
