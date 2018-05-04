from Event import Event
from EventTypes import EventTypes


class ExitClass(Event):
    def __init__(self, student, class_number):
        super(ExitClass, self).__init__(EventTypes.ENTER_CLASS)
        self.student = student
        self.class_number = class_number
