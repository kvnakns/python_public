


# args and kwargs example

def book_trip(*destinations, **options):  # arbitrary words for *args and **kwargs
    print("Destinations:", destinations)
    print("Options:", options)


# Call the function with multiple destinations and options
book_trip("Paris", "Tokyo", "New York", hotel="4-star", flights_included=True, meals="all-inclusive")




#example: 
#   same as above but using 'args' and 'kwargs' instead of 'destinations' and 'options'

def book_trip(*args, **kwargs):
    print("Destinations:", args)
    print("Options:", kwargs)


# Call the function with multiple destinations and options
book_trip("Paris", "Tokyo", "New York", "Singapore", hotel="4-star", flights_included=True, meals="all-inclusive")



# Explanations for further understanding:

# *args: Used when there’s one type of thing with many possible values (like multiple cities of interest). 
# These values are grouped together in a tuple.

# **kwargs: Used when there are multiple, specific things, 
# each with a unique name and value (like hotel="4-star", flights_included, etc). 
# These named values are grouped together in a dictionary.


# This example shows how *args (destinations) collects multiple items under a single category, 
#   while **kwargs (options) gathers named settings that customize the trip.

# Summary:
# Use *args for multiple values that fit into a single category (a list of items).
# Use **kwargs for specific settings or options that each need a label to understand (a dictionary of named parameters).


print("\n")

def Trip(*args, **kwargs):
    print(args)


# Call the function with multiple destinations and options
Trip("Paris", "Tokyo", "New York", "Singapore")

