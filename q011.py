# given a list of words and a word find all the anagrams of the given word
# that are contained in the list of words

def find_anagrams(words, word):
  # first we build a hash table that maps the sorted characters of a word to a list of
  # words containing the same characters and character frequencies (aka annagrams)
  dictionary = {}
  for w in words:
    key = ''.join(sorted(w))
    if not key in dictionary:
      dictionary[key] = []
    dictionary[key].append(w)
  if word in dictionary:
    return dictionary[word]
  else:
    return []
