import random
import hangmanlib
from replit import clear
hangman_word = random.choice(hangmanlib.words)

print("welcome to animal hangman\n\n", hangmanlib.logo)
user_word = []
for a in range(0, len(hangman_word)):
  user_word.append("_")

failed_attempts = 0

while "_" in user_word:
  if failed_attempts < 7:
    print(user_word)
    print(hangmanlib.HangmanArt[failed_attempts])
  else:
    print(hangmanlib.HangmanArt[failed_attempts])
    print("sorry. you lost!\n.\n.\n.\n.")
    exit()
  user_letter = input("please guess a letter(lowercase): ")
  if user_letter not in hangman_word:
    print("nope!")
    failed_attempts += 1
  i = 0
  for i in range(0,len(hangman_word)):
    if user_letter == hangman_word[i]:
      print('good!')
      user_word[i] = user_letter
  clear()
  
print(hangman_word)
print("you win!\n.\n.\n.\n.")