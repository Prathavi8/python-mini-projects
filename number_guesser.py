import random

top_of_range = input("Enter a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)


    if top_of_range <= 0:
        print("Please type a number larger than 0 next time!")
        quit()

else:
    print("Please type a number next time!")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0


while True:
    guesses += 1
    guess_number = input("Guess a number: ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("Please type a number next time!")
        continue

    if guess_number == random_number:
        print("You got it!")
        break
    elif guess_number > random_number:
            print("You were above the number!")
    else:
            print("You were below the number!")
            

print("You got it in", guesses, "guesses")


