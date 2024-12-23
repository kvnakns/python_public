

# List comprehension with a conditional to get squares of even numbers
squares = [x**2 for x in range(1,11) ]
print(squares)



even_squares = [x**2 for x in range(1,11) if x % 2 == 0]
print(even_squares)



# Example 3:
words = ["hello", "world", "python", "list", "comprehension"]
word_lengths = [len(word) for word in words]
print(word_lengths) 





#test
times_two = [x*2 for x in range(1,7)]
print(times_two)