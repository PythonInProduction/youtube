import cupy as cp
x = cp.arange(10_000_000, dtype=cp.float64)
y = cp.ones_like(x)
y = 4.0 * x + y
