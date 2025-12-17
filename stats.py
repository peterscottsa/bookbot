def sort_on(items):
    return items["num"]

def get_sorted_char_list(char_dict):
  char_map = []
  for i in char_dict:
    if not i.isalpha():
      continue
    char_map.append({ "char": i, "num": char_dict[i] })
  return sorted(char_map, reverse=True, key=sort_on)

def get_word_count(text):
  words = text.split()
  return len(words)

def get_character_count(text):
  char_dict = {}
  characters = list(text)

  for char in characters:
    key = char.lower()
    char_dict[key] = 1 if not key in char_dict else char_dict[key] + 1
  
  return char_dict

