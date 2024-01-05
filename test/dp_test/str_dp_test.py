import unittest


class TestCase(unittest.TestCase):
    def test_something(self):
        from array_solve.palindrome.longest_sub_palindrome_516 import Solution
        sol = Solution()
        s = "bbbab"
        self.assertEqual(sol.longestPalindromeSubseq(s), 4)
        s = "cbbd"
        self.assertEqual(sol.longestPalindromeSubseq(s), 2)


if __name__ == '__main__':
    unittest.main()
