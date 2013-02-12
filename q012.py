# given an n*m field containing boolean values and a start position, from the start position flip all values 
# that you can reach by going either up, down, left, or right

def bit_flip(field, start_position):
  start_value = field[start_position[0]][start_position[1]]
  stack = [start_position]
  while stack != []:
    pos = stack.pop()
    if field[pos[0]][pos[1]] == start_value:
      field[pos[0]][pos[1]] = not start_value
    for direction in [(1,0),(0,1),(-1,0),(0,-1)]:
      x = pos[0] + direction[0]
      y = pos[1] + direction[1]
      if -1 < x < len(field) and -1 < y < len(field[0]):
        stack.append((x,y))
