from Event import Event
from EventTypes import EventTypes


class Chat(Event):
    def __init__(self, first_student, second_student):
        self.first_student = first_student
        self.second_student = second_student
        super(Chat, self).__init__(EventTypes.CHAT)
