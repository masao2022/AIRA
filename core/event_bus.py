class EventBus:

    def __init__(self):
        self.events = {}


    def subscribe(self, name, callback):

        if name not in self.events:
            self.events[name] = []

        self.events[name].append(callback)



    def emit(self, name, data=None):

        if name in self.events:

            for callback in self.events[name]:
                callback(data)



event_bus = EventBus()