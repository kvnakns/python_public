
# Identifiers (variables):
# no special characters
# not start with number
# no reserved words
# case-sensitive !



# Literals (the value of the variable):


what = 'My  name is me'
print(what)

# use built in type function to see the type for the variable
print(type(what))

# it can be overwritten and have type change
what = 8.8
print(type(what))

what = True
print(type(what))



# Operators (arithmetic, comparison, logical)

# arithmetic
print("\narithmetic:")

a=10
b=4

# + - * /
print(a+b)

# Modulo: gives the remainer after dividing
print(a % b)

#Floor division: basically divides and removes the remainder and rounds down
print(a // b)

# Exponent: 10 ^ 4 for this example
print(a ** b)


# comparison
print("\ncomparison:")

a = 10
b = 4
c = 4

# equal to
print(a == b)
print(b == c)

# not equal to
print(b != c)

# > and <
print(a > b)

# <=
print(b <= c)


# logical
print("\nlogical:")

# AND
print(True and False)
print(True and True)


print(True or False)
print(True or True)


print(not True)
print(not False)



# logical with expressions
print("\nlogical with expressions:")

a = 10
b = 4
c = 4

print( (b >= c) and (b <= c) )
print( (b >= c) and (a <= c) )

print( (b >= c) or (a <= c) )

