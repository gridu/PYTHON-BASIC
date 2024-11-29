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
from datetime import datetime, timedelta


class Teacher:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def create_homework(self, text, days):
        return Homework(text, days)


class Student:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
    
    def do_homework(self, homework):
        if(homework.is_active()):
            print("You still have time")
            return homework
        print("You are late")
        return None


class Homework:
    def __init__(self, task, days) -> None:
        self.text = task
        self.created = datetime.now()
        self.deadline = timedelta(days=days)
    
    def is_active(self):
        now = datetime.now()
        if(now > self.created + self.deadline):
            return False
        return True


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')
    student = Student('Vladislav', 'Popov')
    teacher.last_name  
    student.first_name  

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  
    expired_homework.deadline  
    expired_homework.text  

    
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  
