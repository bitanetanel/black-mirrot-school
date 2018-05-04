from datetime import datetime


class Event(object):
    def __init__(self, event_type, creation_time=None):
        self.creation_time = creation_time or datetime.now()
        self.event_type = event_type