from collections.abc import Callable

def make_running_average() -> Callable[[int], float]:
    total = 0.0
    count = 0
    def update_average(value: int) -> float:
        nonlocal total, count
        total += value
        count += 1
        return total / count
    return update_average

average = make_running_average()
print(average(10))
print(average(20))
print(average(30))
