from collections.abc import Generator

def my_range(start: int, stop: int, step: int = 1, /) -> Generator[int, int | None, int]:
    count = 0
    while start < stop:
        step_back = yield start
        count += 1
        if step_back is not None:
            start -= step_back
        start += step
    return count

def logged_range(start: int, stop: int) -> Generator[int, int | None, None]:
    total = yield from my_range(start, stop)
    print(f"yielded {total} values")

print(list(logged_range(1, 4)))
