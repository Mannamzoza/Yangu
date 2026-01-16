import random

top_of_range = input("Think of a number between 1 & 10 ? :")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("You can't think a n.o")
        quit()
else:
        print("Think of a number between 1 and 10")
        quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("make a guess: ")

    if user_guess.isdigit():
            user_guess = int(user_guess)

    else:
         print("Think of a number between 1 and 10")
         quit()
         continue


    if user_guess == random_number:
        print("You got it")

        break
    
    elif user_guess > random_number:
            print("You were above the number!")
            
    else:
            print("You are below the number !")

print("you got it in", guesses, "guesses")

#r = random.randrange(-5,11)
#print(r)

#m =random.randint(-5,11)
#print(m)