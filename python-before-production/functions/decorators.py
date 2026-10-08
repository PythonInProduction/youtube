def first(_):
    print("1st")

def second(_):
    print("2nd")

@first
@second
def f(): pass
