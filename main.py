import random
import time

WORD_LENGTH = 5

def color_text(text: str, color_number: int = 0):
  if color_number < 0 or color_number > 7:
    color_number = 0
 
  return f'\033[3{color_number}m{text}\033[0m'

def validate_words_list(words: list[str], word_length: int):
  return all(len(w) == word_length for w in words)

def get_words(path: str) -> list[str]:
  try:
    with open(path, 'r') as file:
      words = [line.strip() for line in file.readlines()]
      if not validate_words_list(words, WORD_LENGTH) == True:
        print(f'Failed to get words: {color_text(f'Some words doesn\'t have {WORD_LENGTH} characters', 1)}')
        exit(1)

      return words
  except Exception as e:
    print(f'Failed to get words: {color_text(str(e), 1)}')
    exit(1)

def pick_word(words: list[str]) -> str:
  return random.choice(words)

def validate_guess(word: str, guess: str) -> list[int]:
  word = word.lower()
  guess = guess.lower()
  length = len(word)
  validation_list = [0 for _ in range(length)]
  almost_correct_tracker = {}

  for i in range(length):
    if guess[i] == word[i]:
      validation_list[i] = 1

  for i in range(length):
    for j in range(length):
      if j != i and guess[i] == word[j] and validation_list[i] == 0 and validation_list[j] != 1 and (guess[i] not in almost_correct_tracker or almost_correct_tracker[guess[i]] != j):
        validation_list[i] = 2
        almost_correct_tracker[guess[i]] = j

  for i in range(length):
    if validation_list[i] == 0:
      validation_list[i] = 3

  return validation_list

def check_correct_guess(validation_list: list[int]) -> bool:
  return all(result == 1 for result in validation_list)

def color_guess_result(guess: str, validation_list: list[int]) -> str:
  result_color_mapper = {0: 7, 1: 2, 2: 3, 3: 1}
  colored_guess = ''

  for i in range(len(guess)):
    char = guess[i]
    char_result = validation_list[i]
    color = result_color_mapper[char_result]
    colored_guess += color_text(char, color)

  return colored_guess

def format_time(elapsed_time: int | float):
  unit_multiplier_mapper = {
    's': 1,
    'm': 60,
    'h': 60 * 60,
    'd': 60 * 60 * 24,
  }

  if elapsed_time >= unit_multiplier_mapper['d']:
    formatted_time = elapsed_time / unit_multiplier_mapper['d']
    unit = 'dias' if int(formatted_time) > 1 else 'dia'
  elif elapsed_time >= unit_multiplier_mapper['h']:
    formatted_time = elapsed_time / unit_multiplier_mapper['h']
    unit = 'horas' if int(formatted_time) > 1 else 'hora'
  elif elapsed_time >= unit_multiplier_mapper['m']:
    formatted_time = elapsed_time / unit_multiplier_mapper['m']
    unit = 'minutos' if int(formatted_time) > 1 else 'minuto'
  else:
    formatted_time = elapsed_time / unit_multiplier_mapper['s']
    unit = 'segundos' if int(formatted_time) > 1 else 'segundo'

  return f'{formatted_time:.2f} {unit}' if int(formatted_time) > 1 else f'{formatted_time:.0f} {unit}'

words = get_words('words.txt')
word = pick_word(words)

start_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)

while True:
  guess = input('Advinhe a palavra: ')

  if (len(guess) < WORD_LENGTH):
    print(f'Palpite inválido: {color_text(f'A palavra de ter exatamente {WORD_LENGTH} letras.', 1)}', end='\n\n')
    continue
  
  validation_list = validate_guess(word, guess)
  is_correct_guess = check_correct_guess(validation_list)

  colored_guess = color_guess_result(guess, validation_list)

  print(colored_guess, end='\n\n')

  if is_correct_guess:
    break

end_time = time.clock_gettime_ns(time.CLOCK_MONOTONIC)
time_spent = (end_time - start_time) / 1e9
time_spent_formatted = format_time(time_spent)

print(f'Parabéns! Você acertou a palavra {color_text(word, 4)} em {time_spent_formatted}')