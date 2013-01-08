# find the x-percentile in a given list of numbers

import sys
import random

def swap(l,i,j):
  h = l[i]
  l[i] = l[j]
  l[j] = h

def partition(numbers):
  pivot_index = random.randint(0,len(numbers)-1)
  swap(numbers,0,pivot_index)
  pivot_index = 0
  end = len(numbers) - 1
  while pivot_index < end:
    if numbers[pivot_index] < numbers[pivot_index+1]:
      swap(numbers,pivot_index+1,end)
      end -= 1
    else:
      swap(numbers,pivot_index,pivot_index+1)
      pivot_index += 1
  return numbers[pivot_index], numbers[:pivot_index], numbers[(pivot_index+1):]

# the idea used to determine the percentile in an unsorted list of numbers is similarly 
# to the idea used in quick sort, but instead of going over all created paritions we only
# stay in the partition that contains the percentile
#
# this has an armotized run time of O(n), think about the optimal split being always cutting
# list in half, that would result in the formula sum over all i of len(numbers)/(2^i) comparisons
# in all the paritions, and this number approaches 2n and thus is linear.
def percentile(numbers, perc):
  pivot,left,right = partition(numbers)
  if len(left)+1 == perc:
    return pivot
  if len(left)+1 < perc:
    return percentile(left, perc)
  else:
    return percentile(right, perc-len(left)-1)


if __name__ == '__main__':
  percentile = float(sys.argv[1])
  numbers = [float(x) for x in sys.argv[2:]]
  print percentile(numbers, int(percentile*len(numbers)))  
