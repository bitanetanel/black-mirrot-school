from Event import Event
from EventTypes import EventTypes


class Eat(Event):
    def __init__(self, student):
        self.student = student
        super(Eat, self).__init__(EventTypes.EAT)
