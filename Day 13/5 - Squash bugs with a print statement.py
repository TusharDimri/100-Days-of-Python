# Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# With the help of print statement, fix the bugs if any in the above code.

pages = 0
word_per_page = 0

pages = int(input("Number of pages: "))
print(f"Pages: {pages}")

word_per_page = int(input("Number of words per page: ")) # We had == earlier where it should have been = so it was a logical error.
print(f"Words per page: {word_per_page}")

total_words = pages * word_per_page
print(f"Total Words: {total_words}")
