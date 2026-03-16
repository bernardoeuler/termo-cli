import re

with open('words.txt', 'r') as f:
  words = f.readlines()

filtered_words = filter(lambda w: re.match(r'^[a-zA-Z0-9]{5}$', w), words)
filtered_words = [w.lower() for w in filtered_words]

with open('words-filtered.txt', 'w') as f:
  f.writelines(list(filtered_words))