# Game 1
# Write a program that generates a random number between 1 and 10, then asks the user to guess the number. 
# The program should give the user three attempts to guess correctly. 
# If the user guesses correctly within three attempts, it should print "Congratulations, you guessed it!" 
# Otherwise, it should print "Sorry, you didn't guess it. The correct number was [the correct number]."

import random
name = input("Hi there! What's your name? ")
number = random.randint(1,10)
guessesleft = 3
print("Hi " + name + "! Please guess a number between 1 and 10. You have " +str(guessesleft) + " guesses.")

guess = int(input())
guessesleft -= 1

while number != guess and guessesleft > 0:
  if guess < number:
    print("Your guess is too low :( Please try again. You have " +str(guessesleft) + " guesses left.")
  elif 11 > guess > number:
    print("Your guess is too high :( Please try again. You have " + str(guessesleft) + " guesses left.")
  print("Hey again " + name + "! Please provide another guess between 1 and 10.")

  guess = int(input())
  guessesleft -= 1

if guess == number:
  print("Saly! You got it. Well done")

else:
  print("Oh no! This time you lose :( It's ok, you'll get it next time. The number I was looking for was " + str(number))