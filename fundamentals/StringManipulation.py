

# Sample string for manipulation
text = "Hello, World! Welcome to Python programming."


# 1. Convert to Uppercase
uppercase_text = text.upper()
print(f"Uppercase: {uppercase_text}")


# 2. Convert to Lowercase
lowercase_text = text.lower()
print(f"Lowercase: {lowercase_text}")


# 3. Title Case (each word capitalized)
title_case_text = text.title()
print(f"Title Case: {title_case_text}")


# 4. Swap Case (uppercase to lowercase and vice versa)
swap_case_text = text.swapcase()
print(f"Swap Case: {swap_case_text}")


# 5. Find the Length of the String
text_length = len(text)
print(f"Length: {text_length}")


# 6. Replace a Substring
replaced_text = text.replace("World", "Universe")
print(f"Replaced 'World' with 'Universe': {replaced_text}")


# 7. Check if String Starts with a Certain Substring
starts_with_hello = text.startswith("Hello")
print(f"Starts with 'Hello': {starts_with_hello}")


# 8. Check if String Ends with a Certain Substring
ends_with_period = text.endswith(".")
print(f"Ends with '.': {ends_with_period}")


# 9. Count Occurrences of a Substring
count_o = text.count("o")
print(f"Count of 'o': {count_o}")


# 10. Find Index of First Occurrence of a Substring
index_world = text.find("World")
print(f"Index of 'World': {index_world}")


# 11. Split String into List of Words
split_words = text.split()
print(f"Split into words: {split_words}")


# 12. Join List of Words into a Single String
joined_text = " ".join(split_words)
print(f"Joined back: {joined_text}")


# 13. Remove Leading and Trailing Whitespace
whitespace_text = "   Extra whitespace   "
stripped_text = whitespace_text.strip()
print(f"Stripped whitespace: '{stripped_text}'")


# 14. Check if All Characters Are Alphabetic
is_alpha = "Hello".isalpha()
print(f"Is alphabetic (Hello): {is_alpha}")


# 15. Check if All Characters Are Digits
is_digit = "12345".isdigit()
print(f"Is digit (12345): {is_digit}")


# 16. Concatenate Strings
concat_text = "Hello" + " " + "World!"
print(f"Concatenated text: {concat_text}")


# 17. Repeat a String
repeated_text = "Echo! " * 3
print(f"Repeated text: {repeated_text}")


# 18. Format String Using f-strings
name = "Alice"
age = 30
formatted_text = f"My name is {name} and I am {age} years old."
print(f"Formatted text: {formatted_text}")


# 19. Format String Using format()
formatted_text_format = "My name is {} and I am {} years old.".format(name, age)
print(f"Formatted text with format(): {formatted_text_format}")


# 20. Check if String Contains Only Alphanumeric Characters
alphanumeric_check = "Hello123".isalnum()
print(f"Is alphanumeric (Hello123): {alphanumeric_check}")
