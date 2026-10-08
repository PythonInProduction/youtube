for n in [4, 8, 15, 16, 23, 42]:
    if n == 42:
        print(
            "Answer to the Ultimate Question of Life, "
            f"the Universe, and Everything is {n}."
        )
        break
else:
    print(
        "Yes, Python loops can have an else, "
        "but you won't see this when the loop breaks early"
    )
