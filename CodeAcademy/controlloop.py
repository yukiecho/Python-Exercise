def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()



# another exercise:pyglatin
pyg = 'ay'

original = raw_input('Enter a word:')
word = original.lower()
first = original[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'

# print everything in math class
    import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!


def hotel_cost(nights):
    return 140*nights
    
    
    
def rental_car_cost(days):
    daily_cost = 40
    if days >= 7:
        return days*daily_cost-50
    elif days <7 and days >=3:
        return days*daily_cost-20
    else:
        return days*daily_cost
        
def plane_ride_cost(city):
    if city =="Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475    

def trip_cost(city,days,spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    
    print trip_cost("Los Angeles",5,600)
