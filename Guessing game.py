secret_number = 2
no_of_guesses = 0
guess_limit = 3
while no_of_guesses < guess_limit:
    guess = int(input("Guess>> "))
    no_of_guesses += 1
    if guess == secret_number :
        print("You Won🎉🎊")
        break 
else:
        print("You failed😭😢!")

