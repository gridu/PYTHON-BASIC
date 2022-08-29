"""
Write tests for classes in python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import datetime
import unittest
from python_part_2 import task_classes as tc


class TestClasses(unittest.TestCase):

    def setUp(self) -> None:
        self.teacher1 = tc.Teacher('Franco', 'James')
        self.teacher2 = tc.Teacher('Cooper', 'Bradley')
        self.student1 = tc.Student('Sin', 'Lee')
        self.student2 = tc.Student('McConaughey', 'Elise')
        self.homework1 = self.teacher1.create_homework(
            'Corporate needs you to find the differences between these two pictures',
            3)
        self.homework2 = self.teacher2.create_homework(
            'They\'re the same picture',
            -13)

    def test_teacher_names(self):
        self.assertTrue(self.teacher1.first_name == 'James' and
                        self.teacher1.last_name == 'Franco' and
                        self.teacher2.first_name == 'Bradley' and
                        self.teacher2.last_name == 'Cooper',
                        msg='Incorrect name for a teacher')

    def test_student_names(self):
        self.assertTrue(self.student1.first_name == 'Lee' and
                        self.student1.last_name == 'Sin' and
                        self.student2.first_name == 'Elise' and
                        self.student2.last_name == 'McConaughey',
                        msg='Incorrect name for a student')

    def test_homework_text(self):
        self.assertTrue(
            self.homework1.text == 'Corporate needs you to find the differences between these two pictures' and
            self.homework2.text == 'They\'re the same picture',
            msg='Wrong homework\'s text')

    def test_homework_deadline(self):
        self.assertTrue(
            self.homework1.deadline.strftime("%Y-%m-%d %H:%M") ==
            (self.homework1.created + datetime.timedelta(3)).strftime("%Y-%m-%d %H:%M") and
            self.homework2.deadline.strftime("%Y-%m-%d %H:%M") ==
            (self.homework2.created + datetime.timedelta(-13)).strftime("%Y-%m-%d %H:%M")
        )

    def test_student_doing_homework(self):
        self.assertIsNotNone(self.student1.do_homework(self.homework1))
        self.assertIsNone(self.student1.do_homework(self.homework2))

    def test_is_active_homework(self):
        self.assertTrue(self.homework1.is_active())
        self.assertFalse(self.homework2.is_active())
