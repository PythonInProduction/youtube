import collections
import time

class RateLimiter:
    def __init__(self, max_per_hour):
        self.max_per_hour = max_per_hour
        self._events = collections.deque()

    @property
    def _remaining(self):
        return self.max_per_hour - len(self._events)

    def _expire(self, now):
        while self._events and now - self._events[0] > 3600:
            self._events.popleft()

    def _record(self, now):
        self._events.append(now)

    def allow(self):
        now = time.monotonic()
        self._expire(now)
        if self._remaining <= 0:
            return "blocked"
        self._record(now)
        return "allowed"

class GlobalRateLimiter(RateLimiter):
    global_max_per_hour = 4
    _global_events = collections.deque()

    @classmethod
    def _global_remaining(cls):
        return cls.global_max_per_hour - len(cls._global_events)

    @property
    def _remaining(self):
        return min(super()._remaining, self._global_remaining())

    def _expire(self, now):
        super()._expire(now)
        while self._global_events and now - self._global_events[0] > 3600:
            self._global_events.popleft()

    def _record(self, now):
        super()._record(now)
        self._global_events.append(now)
