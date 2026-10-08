import math
from collections.abc import Iterable, Iterator


class Embedding:
    def __init__(self, values: Iterable[float]) -> None:
        self._values: tuple[float, ...] = tuple(float(v) for v in values)

    def __repr__(self) -> str:
        return f"Embedding({list(self._values)!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Embedding):
            return NotImplemented
        return self._values == other._values

    def __len__(self) -> int:
        return len(self._values)

    def __getitem__(self, i: int) -> float:
        return self._values[i]

    def __iter__(self) -> Iterator[float]:
        return iter(self._values)

    def __add__(self, other: Embedding) -> Embedding:
        return Embedding(a + b for a, b in zip(self, other, strict=True))

    def __truediv__(self, divisor: float) -> Embedding:
        return Embedding(v / divisor for v in self)

    def __matmul__(self, other: Embedding) -> float:
        return sum(a * b for a, b in zip(self, other, strict=True))

    def __abs__(self) -> float:
        return math.sqrt(self @ self)

    def cosine(self, other: Embedding) -> float:
        return (self @ other) / (abs(self) * abs(other))

    # no get_min, get_max, get_mean, or average: min(e), max(e), and statistics.fmean(e)
    # come with __iter__, and the mean of several embeddings is their sum / their count
