word = input("Enter a word to check: ")

if (word[::-1] == word):
    print("Yes!", "\"" + word + "\"", "is a palindrome.")
else:
    print("No.", "\"" + word + "\"", "is not a palindrome.")