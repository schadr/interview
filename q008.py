# repost the first occurence of each character in a string
# the returned string should contain the unique characters in order of first occurence

# s : string
# return : the string containing the unique characters in order of first occurence
def first_occur(s):
  out = ''
  seen = set() # need the set to ensure that we do not use a character twice
               # while guarnteeing constant look up times
  for c in s:
    if not c in seen:
      seen.add(c)
      out += c
  return out
# this method runs in O(n) with n being the length of s, we iterate once over s and 
# ensure that our checks are constant time by using a set


# follow up question:
# the return string should contain the unique characters in order of last occurence
def last_occur(s):
  return first_occur(s.reverse()).reverse()
