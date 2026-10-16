# 4. Read a file, split its content into words, and store them in a list.
#    i. Print the total number of words.
#    ii. Print all unique words.

filename = input("Enter the file name: ")
with open(filename, "r") as f:
    content = f.read()
words = content.split()
print("Total number of words:", len(words))
unique_words = list(set(words))
print("Unique words:", unique_words)
