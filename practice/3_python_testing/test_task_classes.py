"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""

#import task_classes
import pytest
import sys

sys.path.insert(2, '2_python_part_2')

import task_classes
new_student = task_classes.Student("John", "Doe")
new_teacher = task_classes.Teacher("Sam", "Uncle")
expired_hw = task_classes.Homework("This HW is closed", -2)
new_hw = task_classes.Homework("This HW is active", 2)


# testing is_active method
def test_create_expired_hw_passed():
    active_homework = new_teacher.create_homework('Learn functions', 2)
    assert active_homework.is_active() == True

def test_create_expired_hw_failed():
    expired_homework = new_teacher.create_homework('Learn functions', 2)
    if (expired_homework.is_active() == False):
        pytest.fail()

def test_is_hw_active():
    assert new_hw.is_active()==True

def test_is_hw_inactive():
    assert expired_hw.is_active()==False

def test_missed_deadline():
    assert new_student.do_homework(expired_hw) == False

def test_is_on_time():
    assert new_student.do_homework(new_hw) == True
