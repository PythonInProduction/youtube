import collections
import time

class Limit:
    def __init__(self, max_per_hour):
        self.max_per_hour = max_per_hour
        self._events = collections.deque()

    @property
    def remaining(self):
        return self.max_per_hour - len(self._events)

    def expire(self, now):
        while self._events and now - self._events[0] > 3600:
            self._events.popleft()

    def record(self, now):
        self._events.append(now)

class RateLimiter:
    def __init__(self, max_per_hour, *shared_limits):
        self.local_limit = Limit(max_per_hour)
        self.limits = (self.local_limit, *shared_limits)

    @property
    def remaining(self):
        return min(limit.remaining for limit in self.limits)

    def allow(self):
        now = time.monotonic()
        for limit in self.limits:
            limit.expire(now)
        if self.remaining <= 0:
            return "blocked"
        for limit in self.limits:
            limit.record(now)
        return "allowed"
