# for i in range(17):
#     print("{0:>2} in hex is {0:>02x}".format(i))
#
# x = 0x20
# y = 0x0a
#
# print(x)
# print(y)
# print(x * y)
#
# print(0b101010)

# When converting a decimal number to binary, you look for the highest power
# of 2 smaller than the number and put a 1 in that column. You then take the
# remainder and repeat the process with the next highest power - putting a 1
# if it goes into the remainder and a zero otherwise. Keep repeating until you
# have dealt with all powers down to 2 ** 0 (i.e., 1).
#
# Write a program that requests a number from the keyboard, then prints out
# its binary representation.
#
# Obviously you could use a format string, but that is not allowed for this
# challenge.
#
# The program should cater for numbers up to 65535; i.e. (2 ** 16) - 1
#
# Hint: you will need integer division (//), and modulo (%) to get the remainder.
# You will also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power 8.
#
# As an optional extra, avoid printing leading zeros.
#
# Once the program is working, modify it to print Octal rather than binary.

# My Solutions
# binary
# decimal_number = int(input("Enter a number to convert to binary: "))
# max_power_found = False
# max_power = 0
# while not max_power_found:
#     new_max_power = max_power + 1
#     if (2 ** new_max_power) >= decimal_number:
#         break
#     max_power = new_max_power
#
# binary = ''
# if max_power == 0:
#     binary = '0'
# else:
#     for i in range(max_power, -1, -1):
#         power_number = 2 ** i
#         if power_number <= decimal_number:
#             binary += '1'
#             decimal_number %= power_number
#         else:
#             binary += '0'
#
# print("Binary number is " + binary)

# octal
# decimal_number = int(input("Enter a number to convert to octal: "))
# max_power_found = False
# max_power = 0
# while not max_power_found:
#     new_max_power = max_power + 1
#     if (8 ** new_max_power) >= decimal_number:
#         break
#     max_power = new_max_power
#
# octal = ''
# for i in range(0, max_power + 1):
#     quotient = decimal_number // 8
#     remainder = decimal_number % 8
#     octal = str(remainder) + octal
#     decimal_number = quotient
#
# print("Binary number is " + octal)

# Instructor Solution
# binary
# powers = []
# for power in range(15, -1, -1):
#     powers.append(2 ** power)
#
# print(powers)
#
# x = int(input("Please enter a number: "))
#
# printing = False
# for power in powers:
#     bit = x // power
#     if bit != 0 or power == 1:
#         printing = True
#     if printing:
#         print(bit, end='')
#     x %= power

# octal
powers = []
for power in range(15, -1, -1):
    powers.append(8 ** power)

print(powers)

x = int(input("Please enter a number: "))

printing = False
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printing = True
    if printing:
        print(bit, end='')
    x %= power
