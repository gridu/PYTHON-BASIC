"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import datetime
from freezegun import freeze_time
import pytest


import sys
sys.path[0] = '' # necessary to import from a sibling folder
from practice._2_python_part_2.task_classes import Homework, Teacher, Student


def test_homework_init():
    homework: Homework
    with freeze_time('2024-01-10'):
        homework = Homework('task 1', 5)
    assert homework.__dict__ == {
        'text': 'task 1',
        'deadline': datetime.timedelta(days=5),
        'created': datetime.datetime(2024, 1, 10)
    }


def test_homework_is_active():
    active_homework: Homework
    inactive_homework: Homework
    with freeze_time('2024-01-01'):
        active_homework = Homework('task 1', 20)
        inactive_homework = Homework('task 2', 5)
    with freeze_time('2024-01-10'):
        assert active_homework.is_active()
        assert not inactive_homework.is_active()


def test_teacher_init():
    teacher = Teacher('John', 'Smith')
    assert teacher.__dict__ == {
        'first_name': 'John',
        'last_name': 'Smith'
    }


def test_teacher_create_homework():
    teacher = Teacher('John', 'Smith')
    with freeze_time('2024-01-10'):
        assert teacher.create_homework('task 1', 5).__dict__ == Homework('task 1', 5).__dict__


def test_student_init():
    student = Student('John', 'Smith')
    assert student.__dict__ == {
        'first_name': 'John',
        'last_name': 'Smith'
    }


def test_student_do_homework(capfd):
    student = Student('John', 'Smith')
    active_homework: Homework
    inactive_homework: Homework
    with freeze_time('2024-01-01'):
        active_homework = Homework('task 1', 20)
        inactive_homework = Homework('task 2', 5)
    with freeze_time('2024-01-10'):
        assert student.do_homework(active_homework) == active_homework
    out, err = capfd.readouterr()
    assert out == ''
    assert err == ''
    with freeze_time('2024-01-10'):
        assert student.do_homework(inactive_homework) == None
    out, err = capfd.readouterr()
    assert out == 'You are late\n'
    assert err == ''

if __name__ == '__main__':
    pytest.main([__file__])
