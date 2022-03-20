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


class Teacher:
    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name

    def create_homework(self, text, number_of_days_to_complete):
        """request task text and number of days to complete, returns Homework object
                Note that this method doesn't need object itself"""
        return Homework(text, number_of_days_to_complete, datetime.datetime.now())



class Student:
    def __init__(self, first_name, last_name, ):
        self.first_name = first_name
        self.last_name = last_name

    def do_homework(self, homework):
        """ do_homework - request Homework object and returns it,
        if Homework is expired, prints 'You are late' and returns None"""
        if homework.deadline <= datetime.timedelta(days=0, minutes=0, seconds=0):
            print('You are late')
            return None
        else:
            return homework


class Homework:
    def __init__(self, text, deadline, created):
        self.text = text
        self.deadline = datetime.timedelta(deadline)
        self.created = created

    def is_active(self):
        """is_active - check if task already closed
        TODO because it useless
        """


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    print(teacher.last_name)  # Orlyakov
    print(student.first_name)  # Vladislav

    expired_homework = teacher.create_homework('Learn functions', 0)
    print(expired_homework.created)  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text)  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    print(oop_homework.deadline)  # 5 days, 0:00:00

    print(student.do_homework(oop_homework))
    print(student.do_homework(expired_homework))  # You are late
