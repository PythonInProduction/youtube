import collections
import time

sent_at = collections.deque()

def allow_send(max_per_hour):
    now = time.monotonic()
    while sent_at and now - sent_at[0] > 3600:
        sent_at.popleft()
    if len(sent_at) >= max_per_hour:
        return "blocked"
    sent_at.append(now)
    return "allowed"
