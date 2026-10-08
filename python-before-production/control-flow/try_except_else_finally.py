try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Not a number")
else:
    print(f"You entered {x}")
finally:
    print("Goodbye")
