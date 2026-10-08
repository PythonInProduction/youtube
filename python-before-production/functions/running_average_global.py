total: float = 0.0
count: int = 0

def average(value: int) -> float:
    global total, count
    total += value
    count += 1
    return total / count

print(average(10))
print(average(20))
print(average(30))
