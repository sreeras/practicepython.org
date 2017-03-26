def odd_even(number):
    if (number % 2) == 0:
        return "Even"
    return "Odd"

def multipleof4(number):
    if (number % 4) == 0:
        return "a multiple of 4"
    return "not a multiple of 4"

while True:
    try:
        number = int(input("Enter any number of your choice: "))
        break
    except Exception as err:
        print (type(err))
        print (err.args)
        print("Uh! Uh! That was not a number")

print("Entered number is {0}".format(odd_even(number)))
print("Entered number is {0}".format(multipleof4(number)))
