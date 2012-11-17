# remove every character in String A that appreas in String B

import sys

# removes characters in string b from string a
#
# a : string characters should be removed from
# b : characters that should be removed
#
# return : a without characters from b
def remove_from_string(a,b):
  # create a set of characters that need to be removes such that checking of a characters 
  # existence can be done in constant time
  b_chars = set()
  for c in b:
    b_chars.add(c)
  out = ''
  # check for each character in a if it is in b and only keep those that are not
  for c in a:
    if not c in b_chars:
      out += c
  return out

print(remove_from_string(sys.argv[1],sys.argv[2]))
