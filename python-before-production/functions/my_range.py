from collections.abc import Generator

def my_range(start: int, stop: int, step: int = 1, /) -> Generator[int, None, None]:
    while start < stop:
        yield start
        start += step
