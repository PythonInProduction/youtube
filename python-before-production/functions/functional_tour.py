from functools import partial, reduce, singledispatch

def add(x, y):
    return x + y

add_five = partial(add, 5)         # partial: freeze an argument

doubled = list(map(lambda x: x * 2, [1, 2, 3]))           # map: transform
evens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4]))  # filter: select
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])          # reduce: collapse

@singledispatch                    # singledispatch: pick code by type
def describe(value):
    return f"something: {value}"

@describe.register
def _(value: int):
    return f"the integer {value}"
