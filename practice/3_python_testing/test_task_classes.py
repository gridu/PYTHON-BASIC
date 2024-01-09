"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import datetime
import pytest
from unittest.mock import patch

from your_module import Teacher, Student, Homework  # Replace 'your_module' with the actual name of your module

# Mock the current date and time for testing
current_datetime_mock = datetime.datetime(2023, 1, 1, 12, 0, 0)

@pytest.fixture
def mock_current_datetime():
    with patch('datetime.datetime') as mock_datetime:
        mock_datetime.now.return_value = current_datetime_mock
        yield mock_datetime

def test_teacher_create_homework(mock_current_datetime):
    teacher = Teacher('Dmitry', 'Orlyakov')
    homework = teacher.create_homework('Learn functions', 3)

    assert homework.text == 'Learn functions'
    assert homework.deadline == current_datetime_mock + datetime.timedelta(days=3)
    assert homework.created == current_datetime_mock

def test_student_do_homework_on_time(mock_current_datetime):
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    homework = teacher.create_homework('Learn functions', 3)

    with patch('builtins.print') as mock_print:
        student.do_homework(homework)

    mock_print.assert_called_with(f"Doing homework: {homework.text}")

def test_student_do_homework_late(mock_current_datetime):
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    homework = teacher.create_homework('Learn functions', -1)

    with patch('builtins.print') as mock_print:
        student.do_homework(homework)

    mock_print.assert_called_with("You are late")

def test_homework_is_active_before_deadline(mock_current_datetime):
    homework = Homework('Learn functions', current_datetime_mock + datetime.timedelta(days=3), current_datetime_mock)
    assert homework.is_active()

def test_homework_is_active_on_deadline(mock_current_datetime):
    homework = Homework('Learn functions', current_datetime_mock + datetime.timedelta(days=3), current_datetime_mock + datetime.timedelta(days=3))
    assert homework.is_active()

def test_homework_is_not_active_after_deadline(mock_current_datetime):
    homework = Homework('Learn functions', current_datetime_mock + datetime.timedelta(days=3), current_datetime_mock + datetime.timedelta(days=4))
    assert not homework.is_active()