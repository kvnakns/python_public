
print("\nBasic dictionary example:")  # use \n to return
# Dictionary example
word_count = {}
sentence = "Hello world Hello"
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)



print("\nSet example:")  # use \n to return
# Set example
unique_numbers = set([1, 2, 2, 3, 4])
print("Unique numbers:", unique_numbers)




print("\nBook dictionary example:")  # use \n to return

# Creating a dictionary to store information about a book
book_info = {
    "title": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "year_published": 1960,
    "genres": ["Fiction", "Drama", "Classic"]
}

# Accessing values in the dictionary
print("Book Title:", book_info["title"])  # Output: Book Title: To Kill a Mockingbird
print("Author:", book_info["author"])      # Output: Author: Harper Lee
print("Published Year:", book_info["year_published"])  # Output: Published Year: 1960
print("Genres:", ", ".join(book_info["genres"]))  # Output: Genres: Fiction, Drama, Classic

# Adding a new key-value pair
book_info["rating"] = 4.8
print("Updated Book Info:", book_info)
