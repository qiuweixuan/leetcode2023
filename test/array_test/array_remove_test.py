import unittest


class TestCase(unittest.TestCase):
    def test_remove_elem(self):
        from array_solve.remove_elem import Solution
        sol = Solution()
        # 例子1
        nums = [3, 2, 2, 3]
        val = 3
        val = sol.removeElement(nums, val)
        self.assertEqual([2, 2], nums[:val])
        self.assertEqual(2, val)
        # 例子2
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        val = 2
        val = sol.removeElement(nums, val)
        self.assertEqual([0, 1, 3, 0, 4], nums[:val])
        self.assertEqual(5, val)


if __name__ == '__main__':
    unittest.main()
