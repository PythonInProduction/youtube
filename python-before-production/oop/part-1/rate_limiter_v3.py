import collections
import time

class RateLimiter:
    global_max_per_hour = 4
    # one deque for the whole class
    _global_events = collections.deque()

    def __init__(self, max_per_hour):
        self.max_per_hour = max_per_hour
        # one deque per instance
        self._events = collections.deque()

    @staticmethod
    def _expire(events, now):
        while events and now - events[0] > 3600:
            events.popleft()

    def allow(self):
        now = time.monotonic()
        self._expire(self._events, now)
        self._expire(RateLimiter._global_events, now)
        if len(self._events) >= self.max_per_hour:
            return "blocked"
        if len(RateLimiter._global_events) >= RateLimiter.global_max_per_hour:
            return "blocked"
        self._events.append(now)
        RateLimiter._global_events.append(now)
        return "allowed"
