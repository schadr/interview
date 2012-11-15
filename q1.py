# I'm writing a phone app that serves as a Tivo remote. I can search
# for movies on the web and then select the name of the movie and
# then the phone will enter the name of the movie on my Tivo. 
#
# One problem, though: the Tivo remote doesn't have letter keys.
# Instead it has a grid of letters and you must use the left, right,
# up, and down keys to navigate to the appropriate letter, and the
# select key to select the letter.
#
# I need a function that takes the name of the movie to look up and
# the width of the letter grid, and computes the key presses that
# will enter that string on the Tivo grid. The output should be a
# string, with "u", "d", "l", "r", and "!" corresponding to up,
# down, left, right, and select.
#
# For example, with a grid of width 5,
#   a  b  c  d  e
#   f  g  h  i  j
#   k  l  m  n  o
#   p  q  r  s  t
#   u  v  w  x  y
#   z
# the movie "up" would be "dddd!u!".

import sys

def findSequence(movie_name, grid_width):
  current_char = 'a'
  current_sequence = ''
  for destination_char in movie_name:
    current_sequence += computeWay(current_char, destination_char, grid_width) + '!'
    current_char = destination_char
  return current_sequence

def computeWay(current_char, destination_char, grid_width):
  current_x = (ord(current_char) - ord('a')) % grid_width
  current_y = (ord(current_char) - ord('a')) / grid_width
  
  destination_x = (ord(destination_char) - ord('a')) % grid_width
  destination_y = (ord(destination_char) - ord('a')) / grid_width

  sequence = ''
  while current_x - destination_x != 0 or current_y - destination_y != 0:
    if current_x - destination_x > 0:
      sequence += 'l'
      current_x -= 1
    elif current_y - destination_y > 0:
      sequence += 'u'
      current_y -= 1
    elif current_x - destination_x < 0:
      sequence += 'r'
      current_x += 1
    else:
      sequence += 'd'
      current_y += 1
  return sequence

sequence = findSequence(sys.argv[1], int(sys.argv[2]))
print(sequence)
