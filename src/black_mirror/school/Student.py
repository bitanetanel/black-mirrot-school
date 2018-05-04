from black_mirror.constants import DAY_HOURS
from black_mirror.events import EventsLogger, Eat


class Student(object):
    def __init__(self, name, phone, age, school):
        self.name = name
        self.phone = phone
        self.age = age
        self.school = school
        self.schedule = [-1 for i in xrange(DAY_HOURS)] # Set all schedule to unknown class

    def set_class(self, class_number, hour):
        if hour > len(self.schedule):
            raise ValueError("Student has only {} hours in the schedule".format(len(self.schedule)))
        if not self.school.get_class(class_number).has_place:
            raise SystemError("No place left on class {}".format(class_number))
        self.schedule[hour] = class_number
        self.school.get_class(class_number).add_student(self)

    def can_enter_class(self, class_number):
        return class_number in self.schedule

    def eat(self):
        EventsLogger.log(Eat(self))

    def __repr__(self):
        return "Name: {}, Phone: {}, Age: {}".format(self.name, self.phone, self.age)