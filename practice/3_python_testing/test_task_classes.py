"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

from task_classes import *
import unittest

class Test(unittest.TestCase):
    def setUp(self) -> None:
        self.homework = Homework('functions', 10)
        self.teacher = Teacher('Einstein', 'Albert')
        self.student = Student('Lewandowski', 'Robert')
    def test_init(self):
        self.assertEqual(self.homework.text, 'functions')
        self.assertEqual(self.homework.deadline, datetime.timedelta(10))
        self.assertEqual(self.teacher.first_name, 'Albert')
        self.assertEqual(self.student.last_name, 'Lewandowski')
    def test_create_homework(self):
        self.assertIsInstance(self.teacher.create_homework('Squats', 5), Homework)
        with self.assertRaises(ValueError):
            self.teacher.create_homework('Calculus', -5)
    def test_do_homework(self):
        self.assertIsInstance(self.student.do_homework(self.homework), Homework)
        self.assertEqual(self.student.do_homework(Homework('Algebra', 0)), None)
