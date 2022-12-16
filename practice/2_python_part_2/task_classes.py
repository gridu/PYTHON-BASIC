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
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def create_homework(self, task_text, days_complete):
        self.task_text = task_text
        self.days_complete = days_complete

        # checking if teacher method works
        # print(f"I am a homwhork task text %s
        # and days to complete %s"
        # % (self.task_text, self.days_complete))

        return (Homework(self.task_text, self.days_complete))


class Student:
    def __init__(self, last_name, first_name):
        self.last_name = last_name
        self.first_name = first_name

    def do_homework(self, homework):
        if homework.days_complete == 0:
            print('You are late')


class Homework:
    def __init__(self, task_text, days_complete):
        self.text = task_text
        self.days_complete = days_complete
        self.created = datetime.datetime.now()
        self.deadline = ((self.created
                         + datetime.timedelta(days=self.days_complete))
                         - self.created)

        print("I am a HW object")

    def is_active(self):
        print(self.days_complete)
        print("HW is already closed")


if __name__ == '__main__':
    teacher = Teacher('Dmitry', 'Orlyakov')  # crerated an object Teacher
    student = Student('Vladislav', 'Popov')  # crerated an object Teacher
    print(teacher.last_name)  # Daniil
    print(teacher.first_name)  # Petrov

    expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.is_active()
    print(expired_homework.created)
    print(expired_homework.deadline)
    print(expired_homework.text)

    def is_active_homework():
        create_homework_too = teacher.create_homework
        oop_homework = create_homework_too('create 2 simple classes', 5)
        print(oop_homework.deadline)  # 5 days, 0:00:00
        student.do_homework(oop_homework)
        student.do_homework(expired_homework)  # You are late

    is_active_homework()


""" expired_homework = teacher.create_homework('Learn functions', 0)
    expired_homework.created  # Example: 2019-05-26 16:44:30.688762
    expired_homework.deadline  # 0:00:00
    expired_homework.text  # 'Learn functions' 


    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too('create 2 simple classes', 5)
    oop_homework.deadline  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late"""
