# age = int(input("How old are you? "))
#
# # #if (age >= 16) and (age <= 65):
# # if 15 < age < 66:
# #     print("Have a good day at work")
# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# if (some_condition) or (some_weird_function_that_does_stuff()):
#     # do something

# print("""False: {0}
# None: {1}
# 0: {2}
# 0.0: {3}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input("Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# print(not False)
# print(not True)

# age = int(input("How old are you? "))
# if not(age < 18):
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")