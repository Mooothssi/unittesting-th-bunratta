import unittest
from listutil import *
from listutil_test_data import HUGE_LIST_1000, HUGE_LIST_10000


class UniqueFnTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual([], unique([]))

    def test_single_list_single_ele(self):
        self.assertEqual([5], unique([5]))
        self.assertEqual([4], unique([4]))
        self.assertEqual([1], unique([1]))
        self.assertEqual([-112], unique([-112]))

    def test_single_list_duplicated(self):
        self.assertListEqual(['b', 'a'], unique(["b", "a", "a",
                                             "b", "b", "b",
                                             "a", "a"]))
        self.assertListEqual(['c', 'd', 'e', 'b'], unique(["c", "c", "d", "e", "c", "b", "e"
                                                       ]))
        self.assertListEqual([0.34, 0.45, 0, 8, "Python", None], unique([
            0.34, 0.34, 0.45, 0, 0, 8, 0.45, 0.34, "Python", 0.45, 8, 8, 0.34, "Python", None, "Python", None
        ]))

    def test_single_list_huge(self):
        # 1000 random items with some repetitive items
        self.assertListEqual(sorted(list(range(0, 23))), sorted(unique(HUGE_LIST_1000)))
        # 10000 random items with some repetitive items
        self.assertListEqual(sorted(list(range(0, 23))), sorted(unique(HUGE_LIST_10000)))

    def test_single_list_single_nested_duplicated(self):
        self.assertListEqual(sorted([[1], [2], [3]]), sorted(unique([[1], [1], [3], [3], [2], [2], [3]])))
        self.assertListEqual(sorted([[10, 112], [112], [88], [0.2]]), sorted(unique([[10, 112], [112], [88], [0.2]])))

    def test_non_list(self):
        try:
            with self.assertRaises(InvalidTypeException):
                unique("str")
                unique(1.0)
                unique("str")
        except InvalidTypeException:
            pass


if __name__ == "__main__":
    unittest.main()
