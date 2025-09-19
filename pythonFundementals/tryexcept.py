try:
    input_one = int(input("Type in your first number: "))
    input_two = int(input("Type in your second number: "))

    if input_one > input_two:
        print(f"{input_one} is larger than {input_two}.")
    elif input_two > input_one:
        print(f"{input_two} is larger than {input_one}.")
    else:
        print(f"{input_one} and {input_two} are equal.")
except ValueError:
    print(
        "Please insert a valid input. Integers must only be whole numbers, not floating point integers."
    )
finally:
    print("Run again for further comparisons!")
