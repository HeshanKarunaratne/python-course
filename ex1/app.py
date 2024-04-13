def fizz_Buzz(input):
    if (input % 5 == 0 and input % 3 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_Buzz(7))
