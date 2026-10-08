functions = []

for i in range(1, 4):
    def f():
        return i
    functions.append(f)

for f in functions:
    print(f())
