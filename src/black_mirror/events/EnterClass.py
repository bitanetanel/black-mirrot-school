from Event import Event
from EventTypes import EventTypes


class EnterClass(Event):
    def __init__(self, student, class_number):
        super(EnterClass, self).__init__(EventTypes.ENTER_CLASS)
        self.student = student
        self.class_number = class_number
