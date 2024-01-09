"""
Create 3 classes with interconnection between them (Student, Teacher,
Homework)
Use datetime module for working with date/time
1. Homework takes 2 attributes for __init__: tasks text and number of days to complete
Attributes:
    text - task text
    deadline - datetime.timedelta object with date until task should be completed
    created - datetime.datetime object when the task was created
Methods:
    is_active - check if task already closed
2. Student
Attributes:
    last_name
    first_name
Methods:
    do_homework - request Homework object and returns it,
    if Homework is expired, prints 'You are late' and returns None
3. Teacher
Attributes:
     last_name
     first_name
Methods:
    create_homework - request task text and number of days to complete, returns Homework object
    Note that this method doesn't need object itself
PEP8 comply strictly.
"""
import datetime
import typing


class Teacher:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, task_text, days_to_complete):
        created_date = datetime.datetime.now()
        deadline = created_date + datetime.timedelta(days=days_to_complete)
        return Homework(task_text, deadline, created_date)


class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        if homework.is_active():
            print(f"Doing homework: {homework.text}")
        else:
            print("You are late")


class Homework:
    def __init__(self, text, deadline, created):
        self.text = text
        self.deadline = deadline
        self.created = created

    def is_active(self):
        return datetime.datetime.now() <= self.deadline


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')

    print(teacher.last_name)
    print(student.first_name)

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)
    print(expired_homework.deadline)
    print(expired_homework.text)

    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)