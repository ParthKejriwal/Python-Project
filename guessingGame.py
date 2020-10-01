import random
 
print("Welcome to the number guessing game, try to guess the number - between 1 and 100")
 
rand_num = random.randint(1, 100)
count = 0
 
def main():
    guess = int(input("Guess: "))
 
    if guess == rand_num:
        print("Correct")
    if guess > rand_num:
        print("Guess Lower")
        main()
    if guess < rand_num:
        print("Guess Higher")
        main()
 
main()