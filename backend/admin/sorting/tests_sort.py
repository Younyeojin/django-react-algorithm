import unittest

from admin.sorting.models_sort import Sorting

class TestSorting(unittest.TestCase):
    def test_bubble_sort(self):
        instance = Sorting()
        instance.random_arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        array = instance.bubble_sort()
        self.assertEqual(array, [1, 2, 3, 4, 5, 6, 7, 8, 9])
        print(array)

    def test_merge_sort(self):
        arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        arr = Sorting.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_quick_sort(self):
        # param = [9, 8, 7, 6, 5, 3, 2, 4, 1]
        arr = [99, 8, 17, 6, 51, 3, 21, 4, 1, 2, 5, 9]
        # arr1 = Sorting.quick_sort(param)
        arr2 = Sorting.quick_sort(arr)
        self.assertEqual(arr2, [1, 2, 3, 4, 5, 6, 8, 9, 17, 21, 51, 99])
        print(arr2)