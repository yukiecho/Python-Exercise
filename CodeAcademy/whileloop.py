count = 0

if count < 5:
    print "Hello, I am an if statement and count is", count
    
while count < 5:
    print "Hello, I am a while and count is", count
    count += 1
    
    
# another example for while/else loop
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
    
# another one
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
guess = int(raw_input("Your guess:"))

while guesses_left > 0:
    guesses_left -=1
    if guess == random_number:
        print "you win!"
        break

else:
    print "You lose."
    
# another one
phrase = "A bird in the hand..."

for char in phrase:
    if char == "A" or char =="a":
        print "X",
    else:
        print char,
#Include a comma after the character to be printed in order to ensure it's not printed on its own line, like so:
