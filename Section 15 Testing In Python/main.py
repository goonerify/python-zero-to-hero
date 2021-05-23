"""The main class"""


def do_stuff(num):
    """Add 5 to any number"""
    try:
        return int(num) + 5
    except ValueError as err:
        return err
