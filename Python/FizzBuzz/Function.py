print("Welcome to FizzBuzz!")
def fizzbuzz(number):
    if number % 3 == 0 and number % 7 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 7 == 0:
        return "Buzz"
    else:
        return str(number)

limit = int(input())
print(fizzbuzz(limit)) 
