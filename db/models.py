from db import db_handler
class School:
    pass


class Admin:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def save(self):
        db_handler.save_data(self)


class Student:
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd


class Course:
    pass


class Teacher:
    pass
