squares = [x**2 for x in range(1,11)]

filter(lambda x: x >= 30 and x <= 70, squares)
#Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
