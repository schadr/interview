# 
# write a power function (without using anything like Math.pow) that computes the x^y
#
# things to what out for in this task is to recognize corner cases and be faster
# than the straight forward O(n) algorithm

import sys

def pow(x,y):
  if y < 0:
    return 1 / _pow(x,-y)
  else:
    return _pow(x,y)

def _pow(x,y):
  if y == 0:
    return 1
  if y == 1:
    return x
  if y % 2 == 0:
    return _pow(x*x,y/2)
  else:
    return x*_pow(x*x,y/2)

print(pow(int(sys.argv[1]),int(sys.argv[2])))
