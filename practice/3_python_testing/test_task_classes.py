"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

import tempfile
import pytest
import datetime
import freezegun

from python_part_2 import task_classes as task

with freezegun.freeze_time("2023-03-22"):
    task_teacher = task.Teacher('Teacher', 'Test') 
    task_student = task.Student('Student', 'Test2')
    task_test_active_homework = task_teacher.create_homework('Test Homework', 5)
    task_test_inactive_homework = task_teacher.create_homework('Test Homework', 0)
    task_test_negative_days_h = task_teacher.create_homework('Test Negative Homework', -4)

    class TestTeacher:
        def test_constructor_last_name_assignment(self):
            assert task_teacher.last_name == "Teacher"

        def test_constructor_first_name_assignment(self):
            assert task_teacher.first_name == "Test"

        # Testing if test homework object is of type Homework
        def test_create_homework_type(self):
            assert isinstance(task_test_active_homework, task.Homework)


    class TestStudent:
        def test_constructor_last_name_assignment(self):
            assert task_student.last_name == "Student"

        def test_constructor_first_name_assignment(self):
            assert task_student.first_name == "Test2"

        def test_do_homework_active(self):
            assert task_student.do_homework(task_test_active_homework) == task_test_active_homework

        @pytest.mark.parametrize("hw", [task_test_inactive_homework, task_test_negative_days_h])
        def test_do_homework_inactive_return(self, hw):
            assert task_student.do_homework(hw) is None 

        @pytest.mark.parametrize("hw", [task_test_inactive_homework, task_test_negative_days_h])
        def test_do_homework_inactive_stmt(self, capsys, hw):
            task_student.do_homework(hw)
            captured = capsys.readouterr()

            assert captured.out == "You are late\n"

    class TestHomework:
        def test_homework_return_text(self):
            assert task_test_active_homework.text == "Test Homework"

        def test_homework_return_days(self):
            assert task_test_active_homework.deadline == datetime.timedelta(5)

        def test_homework_created(self):
           assert task_test_active_homework.created == datetime.datetime(2023,3,22)

        def test_is_active_with_active(self):
            assert task_test_active_homework.is_active()
        
        @pytest.mark.parametrize("hw", [task_test_inactive_homework, task_test_negative_days_h])
        def test_is_active_with_inactive(self, hw):
            assert not hw.is_active()
