import os

nums = [i for i in range(10)]

a = 1
b = 2
print(b, nums)

def baz(a=[]):
  return 0

def aaa(a=[]):
  breakpoint()
  return 1


def foo(b=[]):
  return 1

def bar(a):
  return 1

breakpoint()

import os
filename = os.tmpnam()
with open(filename, 'w') as f:
  pass


def another_test_method():
  f = open("/tmp/.deepsource.toml", "r")
  f.write("config file.")
  f.close()
