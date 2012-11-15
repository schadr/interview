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

# function that computes the way from character to character in the movie name
#
# movie_name : the name of the movie to input to the tivo
# grid_width : the width of the gird layout for the characters
#
# return     : the sequence to move through a movie_name
def findSequence(movie_name, grid_width):
  current_char = 'a'
  current_sequence = ''
  for destination_char in movie_name:
    current_sequence += computeWay(current_char, destination_char, grid_width) + '!'
    current_char = destination_char
  return current_sequence

# to compute the way between two letters, we use the ascii character number and computer the rows 
# and column index of a character by treating the grid_width as wrap around limit. 
#
# current_char      : the character that the cursor is currently at
# desitination_char : the character that the cursers needs to go to
# grid_width        : the width of the gird layout for the characters
#
# return            : the sequence needed to go from current to desination
def computeWay(current_char, destination_char, grid_width):
  # computing the cooridnates of a character is done by using the ascii value - ascii value of 'a'
  # to compute the location of the character in an sorted array of lower case characters:
  #
  #  ord(current_char) - ord('a')
  #
  # using this location we can compute the x and y coordnate with (0,0) being in the upper left 
  # corner by modluo and divide. The location modulo the grid width yields the column whereas
  # dividing yields the row.
  current_x = (ord(current_char) - ord('a')) % grid_width
  current_y = (ord(current_char) - ord('a')) / grid_width
  
  destination_x = (ord(destination_char) - ord('a')) % grid_width
  destination_y = (ord(destination_char) - ord('a')) / grid_width

  sequence = ''
  # these if condiations compute the number of steps the cursor needs to move in each direction
  # note that the order is important as it avoids invalid moves.
  # For instance in the above example moving from 'x' to 'z' requires to first more left and then
  # to move down, because there is no letter below 'x' in the grid
  if current_x - destination_x > 0:
    sequence += 'l' * (current_x - destination_x)
  if current_y - destination_y > 0:
    sequence += 'u' * (current_x - destination_x)
  if current_x - destination_x < 0:
    sequence += 'r' * (destination_x - current_x)
  if current_y - destination_y < 0:
    sequence += 'd' * (destination_y - current_y)
  
  return sequence

# additional notes and thoughts:
#
# as you saw we did never represent the actual grid in the program and computed the location
# of each character on the fly. This assumes that the characters follow the order in the ascci table
# as well as assumes that we only work with lower case letters.
# But it is always a good idea to consider memory constrains and the necessaty of keeping the actual
# information in memory.

sequence = findSequence(sys.argv[1], int(sys.argv[2]))
print(sequence)
