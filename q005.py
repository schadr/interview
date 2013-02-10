# pretty print JSON
# for simplicity assime that the JSOn only contains the following data type:
# string: "asdf"
# integers: 124345
# list: [1, 3, 4]
# dictionary: {"key": "value"}
#
# here is an example of a valid JSON string
# ["level1", {"level2": ["level3", "b", "c"], "level2b": 123}]
#
# for this task you can choose your own pretty jason representation I chose the following: 
# [
#   "level1", 
#   {
#     "level2": 
#     [
#       "level3", 
#       "b", 
#       "c"
#     ],
#     "level2b": 
#     123
#   }
# ]

import sys

# this method formats a json string
#
# s : json string
#
# return : fomrated json string
#
def format_json(s):
  indent_level = 0 # number of spaces indentation
  output = "" # the formated json
  in_string = False
  i = 0
  while i < len(s):
    c = s[i]
    # we need to make sure that our special characters do not appear within a string
    # and we need to make sure that we string character start/end character is not esacped
    if c == '"' and (i == 0 or s[i-1] != "\\"):
      in_string = not in_string
    # print the brakets and increase indentation level in the next line
    if not in_string and c in ['[','{']:
      indent_level += 2
      output += c + "\n" + indent_level*' '
    # print the key value character and line break without changing the indentation level
    elif not in_string and c in [':']:
      output += c + '\n' + indent_level*' '
    # print the closing brakets and lower the level of indentation for the next line
    elif not in_string and c in [']','}']:
      indent_level -= 2
      output += "\n" + indent_level*' '
      output += c
    # print comma and line break without changing indentation level
    elif not in_string and c in [',']:
      output += c + "\n" + indent_level*' '
    # just printing the character
    else:
      output += c
    i += 1
  return output

print(format_json(sys.argv[1]))
