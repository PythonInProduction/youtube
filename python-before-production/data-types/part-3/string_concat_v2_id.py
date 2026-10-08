def build_string(length: int) -> str:
    my_long_string = ""
    for i in range(length):
        my_long_string += str(i)
        print(id(my_long_string))
    return my_long_string
