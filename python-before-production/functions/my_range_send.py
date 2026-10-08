from collections.abc import Generator

def my_range(start: int, stop: int, step: int = 1, /) -> Generator[int, int | None, None]:
    while start < stop:
        step_back = yield start
        if step_back is not None:
            start -= step_back
        start += step
