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
