#!/usr/bin/env python

import random


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
     return random.choice(self.knowledge)

knowledge = [
    "str is a data type in Python",
    "programming is hard, but it's worth it",
    "JavaScript async web request", 
    "Python function call definition",
    "object-oriented teacher instance",
    "programming computers hacking learning terminal",
    "pipenv install pipenv shell",
    "pytest -x flag to fail fast",
]

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []
        
    def learn(self, knowledge):
        self.knowledge.append(knowledge)