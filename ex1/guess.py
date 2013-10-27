
from random import randint

def game():
    name = raw_input("Howdy, what's your name? ")
    print "%s, I'm thinking of a number between 1 and 100. " % name,
    print "Try to guess my number." 
    
    number = randint(1, 100)

    guess = 0
    count = 1 

    while guess != number:
        guess = int(raw_input("Your guess? "))
        if guess < number:
            print "Your guess is too low, try again."
            count += 1
        elif guess > number:
            print "Your guess is too high, try again."
            count += 1
        else:
            print "Well done, %s! You found my number in %d tries." % (name,count) 

game()
