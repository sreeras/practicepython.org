text = input("Enter a string to check if it is a palindrome: ")

if text and (text[:] == text[::-1]):
    print("{0} is a palindrome".format(text))
else:
    print("{0} is a not palindrome".format(text))
