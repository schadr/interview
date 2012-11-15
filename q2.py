#
# input: array of integers 
# input: integer
#
# task: determine if there are two numbers in the array that add up to the target number
#

import sys

# this method converts the list of integers into a hasmap and counts the number of occurences
# in the map to later avoid reporting a pair if there exists only one number that is exaclty 
# half of the target
#
# numbers : array of intergers
# target  : number that two terms from the numbers arrays need to add to
def contains_two_terms(numbers, target):
  h = {}
  # creating a hashmap that counts the occurences of each number in the array of numbers
  for n in numbers: 
    if not h.has_key(n):
      h[n] = 0
    h[n] += 1
  # check for each number in the array if the needed term (target - number) exists in the
  # array 
  for n in numbers:
    if h.has_key(target-n):
      # n*2 = target is a special case where we need to ensure that the number n is contained
      # at least twice in the array of numbers
      if n*2 == target and h[n] > 1:
        print("("+str(n)+","+str(n)+")")
      else:
        print("("+str(n)+","+str(target-n)+")")


numbers = map(int,sys.argv[1:])
contains_two_terms(numbers[1:],numbers[0])
