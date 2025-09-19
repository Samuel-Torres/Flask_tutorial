# Python Built In Functions:
# https://docs.python.org/3/library/functions.html


try:
    input_one = str(input("Type in your first name: "))
    input_two = str(input("Type in your second name: "))

    print(
        f"Length of {input_one} is {len(input_one)}. Length of {input_one} is {len(input_two)}"
    )

    if len(input_one) > len(input_two):
        print(f"{input_one} is longer than {input_two}.")
    elif len(input_two) > len(input_one):
        print(f"{input_two} is longer than {input_one}.")
    else:
        print(f"The length of {input_one} and {input_two} are equal.")
except ValueError:
    print("Please insert a valid input. Names must only contain letters, not integers.")
finally:
    print("Run again for further comparisons!")
