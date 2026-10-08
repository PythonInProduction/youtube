import collections
import time

class RateLimiter:
    def __init__(self, max_per_hour):
        self.max_per_hour = max_per_hour
        self._events = collections.deque()

    def allow(self):
        now = time.monotonic()
        while self._events and now - self._events[0] > 3600:
            self._events.popleft()
        if len(self._events) >= self.max_per_hour:
            return "blocked"
        self._events.append(now)
        return "allowed"
