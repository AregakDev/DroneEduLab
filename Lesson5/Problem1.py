number = int(input("Enter number: "))

if number % 5 == 0 and number % 3 != 0:
    print("Fizz")
elif number % 3 == 0 and number % 5 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")