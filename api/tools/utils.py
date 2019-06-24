from sys import stderr


def debug(*args):
    """
    Prints arguments to stderr
    Needed because flask covers up print statements in routes
     """
    for arg in args:
        print(arg, file=stderr)
