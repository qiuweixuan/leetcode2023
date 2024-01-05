import unittest


class TestCase(unittest.TestCase):
    def test_combine_77(self):
        from tree_solve.combine_solve.combine_77 import Solution,Solution2
        sol = Solution()
        all_result = sol.combine(n=4, k=2)
        print(all_result)
        sol = Solution2()
        all_result = sol.combine(n=4, k=2)
        print(all_result)

if __name__ == '__main__':
    unittest.main()
