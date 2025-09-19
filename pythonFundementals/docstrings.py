"""
# Docstring adds intelesense like string that explains what the function or code does.
"""


def compare_name_length(first_name: str, second_name: str):
    """Compare 2 name lengths and returns which one is longer or they are the same length."""
    try:
        if len(first_name) > len(second_name):
            return f"{first_name} is longer than {second_name}."
        elif len(second_name) > len(first_name):
            return f"{second_name} is longer than {first_name}."
        else:
            return f"The length of {first_name} and {second_name} are equal."
    except ValueError:
        return "Please insert a valid input. Names must only contain letters, not integers."
    finally:
        print("Run again for further comparisons!")
