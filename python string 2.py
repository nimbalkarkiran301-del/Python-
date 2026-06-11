
# Write a Python program to take two strings from the user.
# If both strings are equal, convert them to uppercase and replace first string with second string.
# If they are not equal, convert them to lowercase and join them.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if str1 == str2:
    str1 = str2.upper()
    print(" equal")
    print("Result:", str1)
else:
    result = str1.lower() + str2.lower()
    print(" not equal")
    print("Result:", result)