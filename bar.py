import os

breakpoint()


def foo(a=None):
    print("abc")


def bar(z=None):
    print("useless")
    if not z:
        raise AssertionError
