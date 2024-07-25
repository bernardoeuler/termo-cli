def filter_by_size(file_path: str, size: int):
  with open(file_path, "r") as file:
    words = file.readlines()
    new_words = []
    for index, word in enumerate(words):
      if len(word.replace("\n", "")) == size:
        new_words.append(words[index].lower())
  return new_words

def create_file(file_path: str, words: list[str]):
  with open(file_path, "w") as file:
    file.writelines(words)

def read_lines(file_path: str):
  with open(file_path, "r") as file:
    words = map(lambda word: word.replace("\n", ""), file.readlines())
  return words