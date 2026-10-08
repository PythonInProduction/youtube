from collections.abc import Callable
from collections import deque
from statistics import fmean

def make_moving_average(n: int) -> Callable[[int], float]:
    window = deque(maxlen=n)
    def update_average(value: int) -> float:
        window.append(value)
        return fmean(window)
    return update_average

average = make_moving_average(2)
print(average(10))
print(average(20))
print(average(30))
