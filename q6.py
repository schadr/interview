# input : request_friend list
#         approve_friend list
#         reject_friend list
#         remove_friend list
#
# list contents: user_1, user_2, time
#
# task: compute the current social network of each person

# loads the file with the friend list
# 
# to_parse : filename
#
# return : list containing the file entries
#
def parse_file(to_parse):
  f = open(to_parse,'r')
  lines = f.readlines()
  f.close()
  parsed_list = []
  for line in lines:
    tokens = line.split(", ")
    parse_list.append( (tokens[0],tokens[1],Date.parse(tokens[2])) ) 

# creates the current social metwork for each user
#
# inputs are mentioned above
#
# return : dictionary of dictionary containing pairs of friend and when they were approved
def create_current_network(request_friend, approve_friend, reject_friend, remove_friend):
  approve_list = parse_file(approve_friend)
  remove_list = parse_file(remove_friend)
  
  # creating a sparse matrix (dictionary of dictionary) that records the last date a friend 
  # approved a friend request
  approve_dictionary = {}
  for approval in approve_list:
    if not approve_dictionary.has_key(approaval[0]):
      approval_dictionary[approval[0]] = {}
    if not approacl_dicitonary[approval[0]].has_key(approaval[1]):
      approval_dictionary[approval[0]][approval[1]] = approval[2]
    else:
      latest_time = approval_dictionary[approval[0]][approval[1]]
      if latest_time < approal[2]:
        approval_dictionary[approval[0]][approval[1]] = approval[2]
   # remove all entries from the social network that were removed after an approval was granted
   # note that we need to test both ways of the relationship as the removal can come from either
   # side
   for removal in remove_list:
     if approval_dictionary.has_key(removal[0]):
       if approval_dictionary[removal[0]].has_key(removal[1]):
         latest_time = approval_dictionary[removal[0]][removal[1]]
         if latest_time < removal[2]:
           del approval_dictionary[removal[0]][removal[1]]
     elif approval_dictionary.has_key(removal[1]):
       if approval_dictionary[removal[1]].has_key(removal[0]):
         latest_time = approval_dictionary[removal[1]][removal[0]]
         if latest_time < removal[2]:
           del approval_dictionary[removal[1]][removal[0]]
   return approacal_dictionary

# additional notes:
#
# The run time of this algorithm is O(n+m) with n being the size of the approval list and m
# the size of the remove list. We first need to read in both lists, which sets O(n+m) already
# as the minimum complexity. To build the dictionary of dictionaries we need to again iterate
# over both lists once while inserting and removing from the dictionary of dictionaries takes
# constant time
