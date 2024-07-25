from utils.filehandling import read_lines
from utils.colors import green, yellow, black
from random import choice

words = list(read_lines("words-5.txt"))
word = choice(words)
validation = [-1, -1, -1, -1, -1]
attempts = 0

print(f"A palavra é {word}")

while True:
  if attempts == 0:
    guess = input("Digite uma palavra: ").strip().lower()
  else:
    guess = input("Tente novamente: ").strip().lower()

  for i in range(len(word)):
    j = word.find(guess[i], i)
    if j >= 0:
      validation[i] = j

  chars = {}
      
  for guess_index, word_index in enumerate(validation):
    char = guess[guess_index]
    if char not in chars:
      chars[char] = {}
    if guess_index == word_index:
      if "correct" in chars[char]:
        chars[char]["correct"] += 1
      else:
        chars[char]["correct"] = 1
    elif char in word and chars[char]["correct"] < word.count(char):
      if "outplace" in chars[char]:
        chars[char]["outplace"] += 1
      else:
        chars[char]["outplace"] = 1
    elif char not in chars:
      chars[char]["correct"] = 0
      chars[char]["outplace"] = 0
      
  result = ""

  for index, char in enumerate(guess):
    if "correct" in chars[char] and chars[char]["correct"] > 0 and char == word[index]:
      result += green(char)
      chars[char]["correct"] -= 1
    elif "outplace" in chars[char] and chars[char]["outplace"] > 0 and char != word[index]:
      result += yellow(char)
      chars[char]["outplace"] -= 1
    else:
      result += black(char)

  print(result)
    
  attempts += 1
  
  if guess == word:
    break

print(f"A palavra foi {result}")

if guess == word:
  print(f"Você acertou em {attempts} tentativas.")