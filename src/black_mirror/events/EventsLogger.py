class EventsLogger(object):
    events = {}

    @staticmethod
    def log(event):
        if not event.event_type in EventsLogger.events:
            EventsLogger.events[event.event_type] = []
        EventsLogger.events[event.event_type].append(event)