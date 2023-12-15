import unittest


class TestCase(unittest.TestCase):
    def test_gcd_365(self):
        from math_solve import gcd_365
        sol = gcd_365.Solution()
        self.assertEqual(True, sol.canMeasureWater(3, 5, 4))
        self.assertEqual(False, sol.canMeasureWater(2, 6, 5))
        self.assertEqual(True, sol.canMeasureWater(1, 2, 3))

    def test_gcd_914(self):
        from math_solve import gcd_group_size_365
        sol = gcd_group_size_365.Solution()
        self.assertEqual(True, sol.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
        self.assertEqual(False, sol.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))


if __name__ == '__main__':
    unittest.main()
