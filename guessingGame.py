import random
number = random.randint(1, 99)

playerName = input("Hello, What's your name?")
numberOfGuesses = 0
print('Okay! '+ playerName+ ' I am Thinking of a number between 1 and 99.Please try to guess it:')

while numberOfGuesses < 5:
    guess = int(input())
    numberOfGuesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(numberOfGuesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
