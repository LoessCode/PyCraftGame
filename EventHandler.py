global eventQueue, ANIM_eventQueue
eventQueue = {}
ANIM_eventQueue = {}

class Event():
    def __init__(self, key, state, execTimes=None, timePeriod=1, deltaTime = 0):
        self.key = key
        self.state = state
        self.execTimes = execTimes
        self.timePeriod = timePeriod
        self.deltaTime = deltaTime

def addEvent(queue, event):
    if queue == 'EQ':
        eventQueue[event.key] = event
    elif queue == 'AQ':
        ANIM_eventQueue[event.key] = event