from statistics import fmean

values: list[int] = []

def average(value: int) -> float:
    values.append(value)
    return fmean(values)

print(average(10))
print(average(20))
print(average(30))
