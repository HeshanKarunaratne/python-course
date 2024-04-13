## Documentation

#### Primitive Types
- Number
- Boolean
- String

~~~py
students_count = 1000
rating = 4.99
is_published = True
course_name = "Python"
~~~

#### Strings
~~~py
course_name = "Python"
print(len(course_name))
print(course_name[0:2])
print(course_name[-1])
print(course_name[0:])
print(course_name[:5])
print(course_name[:])
~~~

#### Formatted Strings
~~~py
first = "Heshan"
last = "Karunaratne"
full = f"{first} {last}"
print(full)
~~~

#### String Methods
~~~py
first = " Heshan   Karunaratne      "
print(first.upper())
print(first.lower())
print(first.title())
print(first.strip())
print(first.find("shan"))
print(first.replace("a", "z"))
print("shan" in first)
print("sos" not in first)
~~~

#### Numbers
~~~py
import math

print(round(2.9))
print(abs(-2.9))
print(math.ceil(2.2))

print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
~~~

#### Input
~~~py
x = input("x: ")
y = int(x) + 3
print(x)
print(y)
~~~

#### Falsy
- ""
- 0
- None
    - eg
        - bool(0): True
        - bool("False"): True

#### Type Conversions

- int("1")
- float("2.9")
- str(1)

##### If-else
~~~py
temparature = 10
if temparature > 30:
    print("Hot")
elif temparature > 20:
    print("Nice")
else:
    print("Cold")

print("Completed")
~~~

#### Ternary Operator
~~~py
age = 17
message = "Eligible" if age >= 18 else "Not Eligible"
print(message)
~~~

#### Logical Operators
~~~py
high_income = False
good_credit = True
student = False
if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not Eligibile")
~~~

#### For Loops
~~~py
for number in range(1, 10, 2):
    print("Attempting", number, (number) * ".")
~~~

#### For-else
~~~py
successful = True
for number in range(3):
    print("Attempting")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times")
~~~

- Exercise
~~~py
count = 0
for number in range(1, 10):
    if (number % 2 == 0):
        print(number)
        count += 1
else:
    print(f"We have {count} even numbers")
~~~

#### Functions
~~~py
def greet(first_name, last_name):
    print(f"Hi Welcome {first_name} {last_name}")


def get_greeting(first_name, last_name):
    return f"Hi Welcome {first_name} {last_name}"


print(get_greeting("Heshan", "Karunaratne"))
greet("Heshan2", "Karunaratne2")
~~~

#### Optional parameters
~~~py
def increment(number, by=1):
    return number + by


print(increment(10, 5))
~~~

#### Tuples: Collection of objects which cannot be modified
~~~py
def increment(*numbers):
    print(numbers)


increment(2, 3, 4, 5)
~~~

#### Key value pairs
~~~py
def save_user(**user):
    print(user["name"])


save_user(id=1, name="Heshan", age=29)
~~~

- Question: FizzBuzz algorithm
~~~py
def fizz_Buzz(input):
    if (input % 5 == 0 and input % 3 == 0):
        return "FizzBuzz"
    if (input % 3 == 0):
        return "Fizz"
    if (input % 5 == 0):
        return "Buzz"
    return input


print(fizz_Buzz(7))

~~~