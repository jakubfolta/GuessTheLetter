#! python3
import random
import time

def intro():
    print('You would have to guess the letter from the alphabet in 8 guesses. But don\'t worry, I will give you some hints with every guess you take. ;)\n')
    time.sleep(2)
    print('Alright, let\'s start and good luck!\n')
    time.sleep(1)

def guessing():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  random_letter = random.choice(letters)

  chances = 8
  total_chances = 8
  while chances > 0:
    print()
    print(letters)
    print()
    guess = input('About which letter I\'m thinking about?: ')
    print()
    if len(guess) != 1:
      print('Type only one letter from the alphabet!')
      time.sleep(1)
      continue
    elif guess not in letters:
      print('Type only letters, and the ones which you didn\'t try before!')
      time.sleep(1)
      continue
    else:
      chances -= 1
      if letters.index(guess) < letters.index(random_letter):
        print('My letter is further in the alphabet. Try Again.')
        time.sleep(1)
        letters[letters.index(guess)] = '-'
      elif letters.index(guess) > letters.index(random_letter):
        print('My letter is earlier in the alphabet. Try again.')
        time.sleep(1)
        letters[letters.index(guess)] = '-'
      elif letters.index(guess) == letters.index(random_letter):
        time.sleep(1)
        break
    
  chances = total_chances - chances
  
  if letters.index(guess) == letters.index(random_letter):
    print('GREAT, you guessed my letter in', str(chances)+ ' guesses!')
    print()
  elif letters.index(guess) != letters.index(random_letter):  
    print('SORRY, my letter was', random_letter + '.')
    print()
    
intro()
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
  guessing()
  playAgain = input('Would you like to play again? Type "yes" if you would: ')
print()
time.sleep(1)
print('Alright. See you later aligathor!!! ;)')
time.sleep(2)
exit()



