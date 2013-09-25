import random

name = raw_input("Hi! What is your name? ")

print "%s, I'm thinking of a number between 1-100. Try and guess!" % name

answer = random.randint(1,100)

guess = 0
count = 1

while guess != answer:
    guess = int(raw_input("Your guess? "))
    if guess > answer:
        print "Your guess is too high. Try again."
        count += 1
    elif guess < answer:
        print "Your guess is too low. Try again."
        count += 1
    else:
        print "You won in %d tries!" % count
