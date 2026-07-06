"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

from datetime import timedelta

import pytest

from practice.m2_python_part_2 import task_classes


class TestTeacher:
    def setup_method(self, method):
        self.teacher = task_classes.Teacher("Mark", "Willy")

    def test_create_homework_with_positve_days(self):
        homework = self.teacher.create_homework("Lorem", 3)
        assert isinstance(homework, task_classes.Homework)
        assert isinstance(homework.deadline, timedelta)
        assert homework.is_active()

    def test_create_homework_with_negative_days(self):
        with pytest.raises(task_classes.NegativeDaysToCompleteException):
            self.teacher.create_homework("Lorem", -3)


class TestStudent:
    def test_init(self):
        student = task_classes.Student("Adam", "Smith")
        assert isinstance(student, task_classes.Student)
        assert student.first_name == "Adam"
        assert student.last_name == "Smith"

    def test_do_homework_on_time(self):
        student = task_classes.Student("Adam", "Smith")
        homework = task_classes.Homework("Lorem", 10)
        homework = student.do_homework(homework)
        assert isinstance(homework, task_classes.Homework)

    def test_do_homework_late(self, capfd):
        student = task_classes.Student("Adam", "Smith")
        homework = task_classes.Homework("Lorem", -10)
        homework = student.do_homework(homework)
        assert homework is None
        out, err = capfd.readouterr()
        assert "You are late" in out


class TestHomework:
    def test_init(self):
        homework = task_classes.Homework("Lorem", 5)
        assert isinstance(homework, task_classes.Homework)

    def test_is_active_past_dealine(self):
        homework = task_classes.Homework("Lorem", -10)
        assert not homework.is_active()

    def test_is_active_before_dealine(self):
        homework = task_classes.Homework("Lorem", 10)
        assert homework.is_active()
