from basic.config import *
import datetime
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __lt__(self, other):
        if self.year != other.year:
            return self.year < other.year
        if self.month != other.month:
            return self.month < other.month
        return self.day < other.day
    def __eq__(self, value):
        if self.year != value.year:
            return False
        if self.month != value.month:
            return False
        return self.day == value.day
    def __str__(self):
        return f"{self.year}-{self.month}-{self.day}"
    @staticmethod
    def now():
        now = datetime.datetime.now()
        return Date(now.year, now.month, now.day)

class Memory:
    def __init__(self, date, full_content):
        self.date = date
        self.full_content = full_content
        self.abstract = ""
        self.vector = None
        self.importance = 0
        self.importance_reduce=config.IMPORTANCE_INITIAL_REDUCE
        self.role = []

class Memorys:
    def __init__(self):
        self.memories = []

class People:
    def __init__(self, name, know_time, description, relation):
        self.name = name
        self.know_time = know_time
        self.description = description
        self.relation = relation