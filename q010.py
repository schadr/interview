# on an n by n boggle field find the longest possible word

# dictoinary class that contains the words and can check whether a given string
# is a prefix to at least on word in the dictionary
#
# I did not implement the diciotnary as it wasn't part of the original interview
# question but by it self I think it might be good practice
class Dictionary:
  def __init__(self, words):
    pass

  def is_word(self,word):
    pass

  def is_prefix(self,word):
    pass

def find_longest_word(field, dictionary):
  # _find_longest traverses the boggle field using dfs
  def _find_longest(position,current_word):
    if dictionary.is_word(word) and len(word) > len(longest_word):
      longest_word = current_word
    if not dictionary.is_prefix(current_word):
      return
    # from any given field we can go into 8 directions
    for direction in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,-1)]:
      if  -1 < poistion[0] + direction[0] < len(field) and -1 < position[1] + direction[1] < len(field[0]):
        x = poistion[0] + direction[0]
        y = position[1] + direction[1]
        if not visited_field[x][y]:
          visited_field[x][y] = True
          _find_longest((x,y),current_word + field[x][y])
          visited_field[x][y] = False

  # we need to go through each start position to check
  start_positions = [(x,y) for x in range(len(field)) for y in range(len(field[0])]
  longest_word = ''
  visited_field = [ [False for i in range(len(field[0]))] for j in range(len(field)) ]
  for start_position in start_positions:
    _find_longest(start_position, field[start_position[0],start_position[1])       
