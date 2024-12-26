

# Importing a Module from the Basics.py file
# Basically, I created a function called add_numbers there and can now call it from this py script

# Looks like it will import to this file and output anything from Basics.py that is not a function
#       (which is why when I run this script it returns more than just the add_numbers function result)

from Basics import add_numbers 

add_numbers(105, 88)

# try to see if greeting() works
#greeting()  # it does not


# import multiple
#from Basics import (add_numbers, greeting,find_square)

#greeting()

#square = find_square(100)
#print('Square:', square)