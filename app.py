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

  result = ""
      
  for guess_index, word_index in enumerate(validation):
    if guess_index == word_index:
      result += green(guess[guess_index])
    elif guess[guess_index] in word:
      result += yellow(guess[guess_index])
    else:
      result += black(guess[guess_index])

  print(f"Resultado: {result}")
    
  attempts += 1
  
  if guess == word:
    break

print(f"A palavra foi {result}")

if guess == word:
  print(f"Você acertou em {attempts} tentativas.")