# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialise a string variable with the string.


input_string = input("Enter a string to process")
vowel_set = frozenset("aeiou")

consonant_set = set(input_string)

consonant_set.difference_update(vowel_set)
print(sorted(consonant_set))

