import unittest
import sys
sys.path.append('/admin/sorting')

from admin.sorting.models_oop import Calculator, Grade


class TestCalculator(unittest.TestCase):
    def test_calculator(self):
        instance = Calculator()
        instance.num1 = 10
        instance.num2 = 5
        print(instance.add())
        print(instance.subtract())
        print(instance.multiple())
        print(instance.divide())


# class TestPerson(unittest.TestCase):
#     pass


class TestGrade(unittest.TestCase):
    def test_avg(self):
        grade = Grade(60, 80, 70, 'Han')
        # print(grade.return_grade())
        self.assertEqual(grade.name, 'Han')
        self.assertEqual(grade.return_grade(), 'C')


if __name__ == '__main__':
    unittest.main
