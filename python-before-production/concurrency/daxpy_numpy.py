import numpy as np
x = np.arange(10_000_000, dtype=np.float64)
y = np.ones_like(x)
y = 4.0 * x + y
