from collections import deque
from collections.abc import Generator
from statistics import fmean

def moving_average(n: int) -> Generator[float, int, None]:
    window = deque(maxlen=n)
    while True:
        value = yield fmean(window) if window else 0.0
        if value is not None:
            window.append(value)

average = moving_average(2)
next(average)
print(average.send(10))
print(average.send(20))
print(average.send(30))
