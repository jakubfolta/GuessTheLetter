import random
import time

def intro():
  print('Hi there! Would you like to play in a "Guess the letter" game?')
  time.sleep(1)
  print()
  answer = input('Please type: "yes" or "no" ')
  if answer == 'yes' or answer == 'y':
    print()
    print('You would have to guess the letter from the alphabet in 8 guesses. But don\'t worry, I will give you some hints with every guess you take. ;)\n')
    time.sleep(2)
    print('Alright, let\'s start and good luck!\n')
    time.sleep(1)
  elif answer == 'no' or answer == 'n':
    print('No problem, bye bye!')
    time.sleep(2)
    exit()
  else:
    print('I see you\'re bored with this game ;(. Ok, have a nice day!')
    time.sleep(2)
    exit()

def guessing():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']
  random_letter = random.choice(letters)
  while range < 1:
    for chances in range(8):
      print()
      print(letters)
      guess = input('About which letter I\'m thinking about?: ')
      if guess not in letters:
        print('Type one of the letters from the alphabet!')
      
      else:
        if letters.index(guess) < letters.index(random_letter):
          print('My letter is further in the alphabet.')      
        elif letters.index(guess) > letters.index(random_letter):
          print('My letter is earlier in the alphabet')      
        elif letters.index(guess) == letters.index(random_letter):
          break
    
    chances = chances + 1
  
    if letters.index(guess) == letters.index(random_letter):
      print()
      print('Great, you guessed my letter in', str(chances)+ ' guesses!')    
    elif letters.index(guess) != letters.index(rand_letter):  
      print()
      print('Sorry, my letter was', random_letter + '.')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
  intro()
  guessing()
  playAgain = input('Would you like to play again? Type "yes" if you would: ')
print()
time.sleep(1)
print('Alright. See you later aligathor!!! ;)')
time.sleep(2)
exit()






intro()
