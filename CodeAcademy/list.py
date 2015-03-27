suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]            # Third and fourth items (index two and three)
last   = suitcase[4:6]             # The last two items (index four and five)
# the index must one bigger than the real index, so first = index[0:2], actually it only print 2 elements

# Write a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list
start_list = [5, 3, 1, 2, 4]
square_list = []

for start in start_list:
    square_list.append(start**2)
    
    square_list.sort()
print square_list

# add new elements to dictionary
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']
# Your code here: Add some dish-price pairs to menu!
menu['Fish'] = 20.00
menu['penne'] = 12.30
menu['vodka'] = 44

print "There are " + str(len(menu)) + " items on the menu."
print menu

inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell','strange berry','lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold']+=50
