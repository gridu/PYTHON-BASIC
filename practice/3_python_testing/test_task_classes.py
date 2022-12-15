"""
Write tests for classes in 2_python_part_2/task_classes.py (Homework, Teacher, Student).
Check if all methods working correctly.
Also check corner-cases, for example if homework number of days is negative.
"""
import pytest 
import datetime

class Teacher:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, task, days_to_complete):
        return Homework(task, days_to_complete)


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if (homework.is_active()):
            return homework
        else:
            print('You are late')
            return None


class Homework:
    def __init__(self, text, days_to_complete):
        self.text = text
        self.created = datetime.datetime.now()
        self.deadline = self.created + datetime.timedelta(days=days_to_complete)

    def is_active(self):
        return self.deadline > datetime.datetime.now()




@pytest.fixture
def teacher():
    return Teacher('Dmitry', 'Orlyakov')

@pytest.fixture
def student():
    return Student('Vladislav', 'Popov')

@pytest.fixture
def expired_homework(teacher):
    return teacher.create_homework('Learn functions', 0)

@pytest.fixture
def oop_homework(teacher):
    return teacher.create_homework('create 2 simple classes', 5)


def test_teacher_name(teacher):
    assert teacher.last_name =='Dmitry' and teacher.first_name == 'Orlyakov'

def test_student_name(student):
    assert student.last_name =='Vladislav' and student.first_name == 'Popov'

def test_expired_homework_deadline(expired_homework):
    #They must be equals due the homework had 0 days to be complete
    assert expired_homework.deadline == expired_homework.created

def test_expired_homework_text(expired_homework):
    assert expired_homework.text  == 'Learn functions'

def test_no_expired_homework(oop_homework):
    #The date when the homework was created + the days to finish the homework
    assert oop_homework.deadline == oop_homework.created + datetime.timedelta(days=5) 

def test_do_homework_expired(student,expired_homework):
    assert student.do_homework(expired_homework) ==  None# You are late

def test_do_homework_on_time(student,oop_homework):
    assert student.do_homework(oop_homework) == oop_homework