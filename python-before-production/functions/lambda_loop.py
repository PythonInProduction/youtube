functions = []

for i in range(1, 4):
    functions.append(lambda: i)

for f in functions:
    print(f())
