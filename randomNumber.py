import random

top_range = input("Enter top of range: ")
counter = 0

if top_range.isnumeric():
    top_range = int(top_range)

    if top_range < 0:
        print("Enter number greater than 0")
        quit()
else:
    print("Enter numerals")
    quit()
r = random.randrange(0, top_range)

#print(r)

while True:
    guess = input("Make a guess: ")
    counter += 1
    if guess.isdigit():
        guess = int(guess)

        if guess == r:
            print("Correct!")
            print("number of times guessed: " + str(counter))
            break
        elif r > guess:
                print("above")
        else:
                print("below")

    else:
        print("please type a number")
        continue     
