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

#### Lists
~~~py
letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + matrix
numbers = list(range(20))
chars = list("Hello")
print(len(chars))
print(numbers[::2])
~~~

#### List packing and unpacking
~~~py
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
first, second, third, *other = numbers

print(first)
print(second)
print(third)
print(other)
~~~

#### Looping: If you need index need to use enumerate() and use list unpacking to extract the tuple
~~~py
letters = ["a", "b", "c"]
for index, letter in enumerate(letters):
    print(index, letter)

~~~

#### Add Remove from List
~~~py
letters = ["a", "b", "c"]

# Add to end
letters.append("d")

# Add at index
letters.insert(0, "-")

# Remove from end
letters.pop()

# Remove from index
letters.pop(0)

# Remove first occurence: without index
letters.remove("a")

# Delete statement
del letters[0:3]

# Remove all
letters.clear()

print(letters)
~~~

#### Finding Items
~~~py
letters = ["a", "b", "d", "c"]
if "d" in letters:
    print(letters.index("d"))
else:
    print("not found")
~~~

#### Sorting Lists
~~~py
numbers = [3, 51, 2, 8, 6]

# Sort Method
numbers.sort(reverse=True)
print(numbers)

# Sorted Function
sorted(numbers)

# Custom sorting
items = [
    ("Product2", 10),
    ("Product1", 20),
    ("Product0", 12)
]

def sort_item(item):
    return item[1]

items.sort(key=sort_item)
print(items)
~~~

#### Lambda Function
~~~py
items = [
    ("Product2", 10),
    ("Product1", 20),
    ("Product0", 12)
]

items.sort(key=lambda item: item[1])
print(items)
~~~

#### Map
~~~py
items = [
    ("Product2", 10),
    ("Product1", 20),
    ("Product0", 12)
]

# General way
prices = []
for item in items:
    prices.append(item[1])


# Using map function which returns an iterable
x = map(lambda item: item[1], items)
for item in x:
    print(item)

# Convert to list
prices = list(map(lambda item: item[1], items))
print(prices)
~~~

#### Filtering
~~~py
items = [
    ("Product2", 10),
    ("Product1", 20),
    ("Product0", 12)
]

filtered = list(filter(lambda item: item[1] > 10, items))
print(filtered)
~~~

#### List comprehension
~~~py
items = [
    ("Product2", 10),
    ("Product1", 20),
    ("Product0", 12)
]

prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]

filtered = list(filter(lambda item: item[1] > 10, items))
filtered = [item for item in items if item[1] > 10]
~~~

#### Zip Function
~~~py
list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip(list1, list2, "abc")))
~~~

#### Stack
~~~py
browsing_session = []
# Push
browsing_session.append(1)

# Pop
browsing_session.pop()

# Peek
if not browsing_session:
    browsing_session[-1]
~~~

#### Queue
~~~py
from collections import deque
queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft()
queue.popleft()

print(queue)
~~~

#### Tuple: Read only list
~~~py
point = tuple([1, 2, 3])
print(point[0:3])

x, y, z = point
print(x)
print(y)
print(z)
~~~

#### Arrays: If you have a large datasets use Arrays
~~~py
from array import array
numbers = array("i", [1, 2, 3])
numbers.append(4)
~~~

#### Sets
~~~py
numbers = [1, 1, 3, 4, 4, 5]
first = set(numbers)
second = {1, 6}

print(first | second)
print(first & second)
print(first - second)
print(first ^ second)
~~~

#### Dictionary
~~~py
point = dict(x=1, y=20)
point['x'] = 10
print(point)
if "a" in point:
    print(point["a"])

print(point.get("a", 100))
del point["x"]

for x in point.items():
    print(x)
~~~

#### Dictionary Comprehensions
~~~py
values = {x: x * 2 for x in range(5)}
print(values)
~~~

#### Generator Expressions
~~~py
from sys import getsizeof

values = (x * 2 for x in range(5))
print(type(values))
print(getsizeof(values))
~~~

#### Unpacking iterables
~~~py
first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 10}
print(combined)
~~~

- Question
~~~py
sentence = "This is a common interview question"
char_frequency = {}
for char in sentence:
    if char == ' ':
        continue
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

char_frequency_sorted = sorted(
    char_frequency.items(),
    key=lambda kv: kv[1],
    reverse=True)
print(char_frequency_sorted[0][0])
~~~

#### Exceptions
~~~py
try:
    file = open("app.py")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()
~~~

#### With statement
~~~py
try:
    with open("app.py") as file:
        print("File opened")
    age = int(input("Age: "))
    xfactor = 10/age
except (ValueError, ZeroDivisionError):
    print("You didnt enter a valid age.")
else:
    print("No exceptions were thrown")
finally:
    file.close()
~~~

#### Raising Exceptions
~~~py
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as ex:
    print(ex)
~~~

#### Class
~~~py
class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))
~~~

#### Constructors
~~~py
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
point.draw()
~~~

#### Class and instance attributes
~~~py
class Point:

    default_color = "red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(10, 20)
point.default_color = "blue"
point.draw()
print(point.default_color)

another = Point(1, 2)
print(another.default_color)
~~~

#### Class and instance methods
~~~py
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()
~~~

#### Magic methods: __str__
~~~py
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

point = Point(1, 2)
print(point)
~~~

#### __eq__
~~~py
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(3, 4)
other = Point(2, 3)
print(point < other)
~~~

#### __add__
~~~py
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x,  self.y + other.y)


point = Point(3, 4)
other = Point(2, 3)
print(point + other)
~~~

### __getitem__, __setitem__, __len__, __iter__
~~~py
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.tags[tag] = self.tags.get(tag, 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud.add("Python")
cloud.add("python")
cloud.add("python")
cloud["vb"] = 10
print(cloud.tags)
print(len(cloud))
~~~

#### Private members
~~~py
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        tag = tag.lower()
        self.__tags[tag] = self.__tags.get(tag, 0) + 1

cloud = TagCloud()
# print(cloud.__tags) This statement will not work now
~~~

#### Properties
~~~py
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price Cannot be negative")
        self.__price = value


product = Product(-10)
~~~

#### Inheritance
~~~py
class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


# Animal: Parent, Base
# Mammal: Child, Sub
class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)
~~~

#### Overriding: super() does not need to be the first statement in python
~~~py
class Animal:
    def __init__(self):
        self.age = 1
        print("Animal Constructor")

    def eat(self):
        print("eat")

class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(m.age)
print(m.weight)
~~~

#### MultiLevel Inheritance
~~~py
class Animal:
    def eat(self):
        print("eat")

class Bird(Animal):
    def fly(self):
        print("fly")
~~~

#### Multiple Inheritance
~~~py
class Flyer:
    def fly(self):
        pass

class Swimmer:
    def swim(self):
        pass

class FlyingFish(Flyer, Swimmer):
    pass
~~~

- Example
~~~py
class InvalidOperationError(Exception):
    pass

class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

~~~

#### Abstract classes
~~~py
from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network")

fileStream = FileStream()
print(fileStream.opened)
fileStream.open()
print(fileStream.opened)
fileStream.close()
print(fileStream.opened)
~~~

#### Polymorphism
~~~py
from abc import ABC, abstractmethod

class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass

class TextBox(UIControl):
    def draw(self):
        print("TextBox")

class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

text = TextBox()
ddl = DropDownList()
draw([text, ddl])
~~~

#### Duck Typing
~~~py
class TextBox:
    def draw(self):
        print("TextBox")

class DropDownList:
    def draw(self):
        print("DropDownList")

def draw(controls):
    for control in controls:
        control.draw()

text = TextBox()
ddl = DropDownList()
draw([text, ddl])
~~~

#### Built In types
~~~py
class Text(str):
    def duplicate(self):
        return self+self

class TrackableList(list):
    def append(self, object):
        print("append called:", object)
        super().append(object)

text = Text("hello")
print(text.duplicate())

tl = TrackableList()
tl.append("l1")
~~~

#### Data Classes: These values are immutable
~~~py
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
~~~