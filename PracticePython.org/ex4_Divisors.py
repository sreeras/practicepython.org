while True:
    try:
        number = int(input("Enter a number, I will return its divisors: "))
        break
    except ValueError:
        print("That was not a number. Try again!!!\n")

##Solution 1
divisors = []
for num in range(1, number+1):
    if number % num == 0:
        divisors.append(num)

print (divisors)

##Solution 2

print ([i for i in range(1, number+1) if (number % i) == 0])